"""One test per inclusion/exclusion rule and per edge case of the decision table in docs/PLAN.md."""

import json
from datetime import date

import pytest

from investordb.registries import RegistryRecord
from investordb.rules import decide

AS_OF = date(2026, 10, 8)  # window for "active" starts 2023-10-08


def reg(active=True, country="CZ"):
    return RegistryRecord("ARES", "12345678", "Test Ventures a.s.", country, "", "121", "2015-01-01",
                          None if active else "2024-05-01")


def claim(field, value, url="https://press.example/a", check="ok", event_date=""):
    return {"field": field, "value": json.dumps(value), "source_url": url, "auto_check": check, "event_date": event_date}


def inv(company, d, url="https://press.example/a", check="ok"):
    return claim("investments", {"company": company, "date": d}, url=url, check=check, event_date=d)


def vc(*extra, types=("vc",), hq="CZ"):
    return [claim("investor_type", list(types)), claim("hq_country", hq), *extra]


STRONG = (inv("Alpha", "2025-03-01", "https://news-one.example/x"), inv("Beta", "2022-06-01", "https://news-two.example/y"))


def test_clear_vc_is_included_tier_a():
    d = decide("C1", vc(*STRONG), reg(), AS_OF)
    assert (d.status, d.tier) == ("INCLUDED", "A")


def test_single_source_domain_gives_tier_b():
    d = decide("C1", vc(inv("Alpha", "2025-03-01"), inv("Beta", "2022-06-01")), reg(), AS_OF)
    assert (d.status, d.tier) == ("INCLUDED", "B")


def test_e2_dissolved_entity():
    assert decide("C1", vc(*STRONG), reg(active=False), AS_OF).reason == "E2"


def test_e2_inactive_more_than_36_months():
    d = decide("C1", vc(inv("Alpha", "2023-01-01"), inv("Beta", "2021-06-01")), reg(), AS_OF)
    assert (d.status, d.reason) == ("REJECTED", "E2")


@pytest.mark.parametrize(
    "type_,code",
    [("crowdfunding_platform", "E3"), ("advisory", "E3"), ("real_estate", "E4"), ("lender", "E4"),
     ("fund_of_funds", "E5"), ("group_holding", "E6"), ("grant_agency", "E9")],
)
def test_non_investor_types(type_, code):
    d = decide("C1", vc(types=(type_,)), reg(), AS_OF)
    assert (d.status, d.reason) == ("REJECTED", code)


def test_e1_self_described_investor_without_investments():
    assert decide("C1", vc(), reg(), AS_OF).reason == "E1"


def test_e1_only_one_investment():
    assert decide("C1", vc(inv("Alpha", "2025-03-01")), reg(), AS_OF).reason == "E1"


def test_e7_name_only_company():
    assert decide("C1", [], reg(), AS_OF).reason == "E7"


def test_failed_quote_checks_do_not_count_as_evidence():
    claims = vc(inv("Alpha", "2025-03-01", check="quote_not_found"), inv("Beta", "2025-01-01", check="url_dead"))
    assert decide("C1", claims, reg(), AS_OF).reason == "E1"


def test_blocked_sources_go_to_review():
    d = decide("C1", vc(inv("Alpha", "2025-03-01", check="blocked")), reg(), AS_OF)
    assert (d.status, d.reason) == ("NEEDS_REVIEW", "REVIEW_BLOCKED")


def test_oos_foreign_hq():
    assert decide("C1", vc(*STRONG, hq="other"), None, AS_OF).reason == "OOS_HQ"


def test_oos_pe_only():
    assert decide("C1", vc(*STRONG, types=("pe",)), reg(), AS_OF).reason == "OOS_TYPE"


def test_unverified_type_goes_to_review():
    claims = [claim("investor_type", ["vc"], check="quote_not_found"), claim("hq_country", "CZ"), *STRONG]
    assert decide("C1", claims, reg(), AS_OF).reason == "REVIEW_TYPE"


def test_missing_registry_record_goes_to_review():
    assert decide("C1", vc(*STRONG), None, AS_OF).reason == "REVIEW_IDENTITY"


# --- edge cases from the decision table ---------------------------------------------------------------

def test_new_fund_with_one_investment_is_included():
    claims = vc(inv("Alpha", "2026-02-01"), claim("funds", {"name": "Fund I", "vintage": "2025"}, event_date="2025-11-01"))
    assert decide("C1", claims, reg(), AS_OF).status == "INCLUDED"


def test_public_vc_direct_investor_is_included():  # e.g. a state programme's direct-investing subsidiary
    assert decide("C1", vc(*STRONG, types=("public_vc",)), reg(country="SK"), AS_OF).status == "INCLUDED"


def test_cvc_investing_into_external_startups_is_included():
    assert decide("C1", vc(*STRONG, types=("cvc",)), reg(), AS_OF).status == "INCLUDED"


def test_platform_that_also_runs_own_fund_is_judged_on_investments():
    assert decide("C1", vc(*STRONG, types=("crowdfunding_platform", "vc")), reg(), AS_OF).status == "INCLUDED"


def test_lux_fund_vehicle_with_czech_team_counts_as_czech():
    # HQ is where the team sits (hq_country claim CZ), not the fund's domicile
    assert decide("C1", vc(*STRONG, hq="CZ"), reg(country="CZ"), AS_OF).status == "INCLUDED"


def test_vc_and_pe_manager_is_in_scope():
    assert decide("C1", vc(*STRONG, types=("pe", "vc")), reg(), AS_OF).status == "INCLUDED"


def test_accelerator_is_out_of_pilot_scope():
    assert decide("C1", vc(*STRONG, types=("accelerator",)), reg(), AS_OF).reason == "OOS_TYPE"
