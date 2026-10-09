"""Regression tests for the problems found in the pre-review audit (docs/DECISIONS.md D30-D33).
Each case is a real record from pilot v1."""

import json

import pytest

from investordb.money import TARGET_FUND
from investordb.pipeline import ticket_eur, total_capital
from investordb.registries import legal_form
from investordb.rules import investments_from
from investordb.validate import deal_context

ON = "2026-10-09"


def fund(name, size, quote, currency="EUR"):
    return {"field": "funds", "auto_check": "ok", "source_url": "https://x.example",
            "value": json.dumps({"name": name, "size": size, "currency": currency}), "quote": quote}


def test_reflex_capital_range_and_number_words():
    # v1 showed "30 €": the closed fund was written in words, the planned one as a range
    cap = total_capital([
        fund("třetí fond", "dvaadvacet milionů eur", "Uzavřel svůj třetí fond o velikosti dvaadvacet milionů eur"),
        fund("Reflex 2", "od 30 do 50 milionů eur", "Reflex 2 by měl mít nakonec od 30 do 50 milionů eur"),
    ], ON)
    assert cap["eur"] == pytest.approx(22e6)
    assert cap["method"] == "sum_of_1_closed_funds"
    assert len(cap["targets"]) == 1


@pytest.mark.parametrize(
    "quote",
    [
        "Aiming to raise €20 million, the fund will support early stage AI-driven companies",  # Look AI Ventures
        "Její nový fond zvaný Rockaway Ventures Fund má cílovou velikost 100 milionů eur",  # Rockaway
        "The new fund is aiming €20 million and is currently looking for investors",  # DEPO
        "Nový fond chce v nejbližší době investovat do celkem 20 ukrajinských startupů přibližně 10 milionů eur",
    ],
)
def test_target_funds_are_not_capital(quote):
    assert TARGET_FUND.search(quote)


def test_closed_fund_with_investment_goal_is_not_a_target():
    # "has a volume of 40 million and a goal to invest in 50 startups" - the fund itself is closed
    assert not TARGET_FUND.search("Váš fond Purple Ventures 2 má objem čtyřicet milionů eur a cíl investovat do více "
                                  "než 50 startupů v období do roku 2028.")


def test_ticket_minimum_borrows_scale_of_maximum():
    lo, hi, flags = ticket_eur({"min": "0,3", "max": "1,5 mil. EUR", "currency": "EUR"}, ON)  # Tilia showed "0 €"
    assert lo == pytest.approx(3e5) and hi == pytest.approx(1.5e6) and not flags


def test_implausible_amounts_are_dropped_and_flagged():
    lo, hi, flags = ticket_eur({"min": "€1", "max": "€2", "currency": "EUR"}, ON)
    assert lo is None and hi is None and flags


PAGE = ("Novinky. Pražský fond N1 investoval do startupu Respeecher v kole seed. " + "x " * 200 +
        "Portfolio: Taikun, Flick, Myriad AI. " + "y " * 200 + "From Prague to Silicon Valley: Taikun's exit to Cloudera.")


def test_investor_mention_is_not_a_deal():
    # regression: a 2026 article calling Miton "an investor" dated a 2020 deal as 2026
    page = "Boataround, backed by its investor Miton, is growing fast. " + "Filler text. " * 60
    assert deal_context("Boataround, backed by its investor Miton", page) == "deal"  # 'backed' is a deal word
    page2 = "Among Boataround's investors is the Czech group Miton. " + "Filler text. " * 60
    assert deal_context("Among Boataround's investors is the Czech group Miton.", page2) == "mention"
    # the real case: a German article about a NEW 2026 round that lists existing investors
    page3 = ("Boataround erhält Millionen in einer neuen Finanzierungsrunde, investiert haben neue Geldgeber. "
             "Zu den Investoren der Firma gehören neben Crowdberry etwa Reflex Capital und Miton gehören.")
    assert deal_context("Zu den Investoren der Firma gehören neben Crowdberry etwa Reflex Capital und Miton gehören.",
                        page3) == "mention"
    # but "new investors such as ... joined the round" is a deal
    assert deal_context("New investors such as Bloomhaus and Look AI Ventures joined the round", "") == "deal"
    # and the syndicate of THIS round is a deal too (i&i Biotech - wrongly a 'mention' in the first audit fix)
    page4 = ("Captain T Cell GmbH announced the successful closing of a seed financing round totaling €8.5 million. "
             "A syndicate of experienced life science investors including i&i Biotech Fund I SCSp, Brandenburg Kapital")
    assert deal_context("A syndicate of experienced life science investors including i&i Biotech Fund I SCSp",
                        page4) == "deal"


def test_deal_context():
    assert deal_context("From Prague to Silicon Valley: Taikun's exit to Cloudera.", PAGE) == "exit"
    assert deal_context("Pražský fond N1 investoval do startupu Respeecher", PAGE) == "deal"
    assert deal_context("Portfolio: Taikun, Flick, Myriad AI.", PAGE) == "mention"


def test_exits_are_not_investments_and_mentions_are_undated():
    claims = [
        {"field": "investments", "value": json.dumps({"company": "Taikun"}), "event_date": "2026-06-20",
         "deal_context": "exit", "source_url": "https://n1.rocks"},
        {"field": "investments", "value": json.dumps({"company": "Productboard"}), "event_date": "2021-09-23",
         "deal_context": "mention", "source_url": "https://cc.cz/a"},
        {"field": "investments", "value": json.dumps({"company": "Apptronik"}), "event_date": "2026-02-13",
         "deal_context": "deal", "source_url": "https://lupa.cz/b"},
    ]
    invs = {i.company: i.date for i in investments_from(claims)}
    assert "Taikun" not in invs
    assert invs == {"Productboard": "", "Apptronik": "2026-02-13"}


def test_attribution_requires_the_candidate_near_the_quote():
    from investordb.validate import attributed

    page = ("Ranketta, a Brno, Czech Republic-based AI visibility platform, has raised €1 million in pre-Seed funding. "
            + "Filler text. " * 80 + "Other news: Pekat Vision got money from Lighthouse Ventures.")
    # Lighthouse is named on the page, but far from the Ranketta quote -> not attributed
    assert not attributed("Ranketta, a Brno, Czech Republic-based AI visibility platform, has raised €1 million",
                          page, ["Lighthouse Ventures"])
    near = "The round was led by Lighthouse Ventures. Ranketta, a Brno-based platform, has raised €1 million."
    assert attributed("Ranketta, a Brno-based platform, has raised €1 million", near, ["Lighthouse Ventures"])
    # punctuation differences in names do not matter
    assert attributed("Xund raised a seed round from J&T Ventures", "Xund raised a seed round from J&T Ventures",
                      ["J&T Ventures"])


@pytest.mark.parametrize(
    "names,text,expected",
    [
        (["i&i Biotech Investments"], "The round was joined by i&i Biotech Fund and others.", True),
        (["ZAKA Ventures"], "We are pleased to welcome DeepSeq to the Zaka VC portfolio", True),
        (["Presto Ventures"], "via its Presto Tech Horizons fund", True),
        (["J&T Ventures"], "Jet Investment led the round", False),  # short core 'j t' must not match
        (["Gi21 Capital"], "Led by Gi21, a Prague-based firm", True),  # core with a digit
        (["Purple Ventures"], "Purpleville Inc. raised a round", False),  # whole words only
    ],
)
def test_name_variants(names, text, expected):
    from investordb.validate import attributed

    assert attributed(text, text, names) is expected


def test_unattributed_investments_do_not_count():
    claims = [{"field": "investments", "value": json.dumps({"company": "AppFactor"}), "event_date": "2026-02-01",
               "deal_context": "deal", "attributed": "0", "source_url": "https://news.example/a"}]
    assert investments_from(claims) == []


@pytest.mark.parametrize("ico", ["28538137", "04753101", "05775574", "03890333", "24269158", "02059533"])
def test_valid_czech_icos_from_the_pilot(ico):
    from investordb.registries import valid_ico

    assert valid_ico(ico, "CZ")


def test_malformed_ico_is_rejected():
    from investordb.registries import valid_ico

    assert not valid_ico("52 524 5311", "SK")  # CB Investment Management's website shows 10 digits
    assert not valid_ico("28538138", "CZ")  # wrong check digit


@pytest.mark.parametrize(
    "registry_name,name,rank",
    [
        ("Credo Ventures a.s.", "Credo Ventures", 0),
        ("Credo Ventures Management II a.s.", "Credo Ventures", None),  # v2 picked this one
        ("Rockaway Ventures Fund SICAV a.s., podfond I", "Rockaway Ventures", 1),
        ("Presto Ventures II a.s., osoba rizikového kapitálu", "Presto Ventures", 1),
        ("ZAKA VC I, osoba rizikového kapitálu, a.s.", "zaka vc", 1),
        ("MITON CZ, s.r.o.", "Miton", 1),
        ("Nation1 Investment s.r.o.", "Nation1", None),  # wrong company in v2
        ("Czech Founders z.ú.", "Czech Founders", None),  # non-profit, never an investor's identity
        ("CB Investments s. r. o.", "CB Investment Management s. r. o.", None),  # wrong company in v2
        ("Czech Founders Ventures s.r.o.", "Czech Founders Ventures s.r.o.", 0),
    ],
)
def test_strict_identity_matching(registry_name, name, rank):
    from investordb.registries import strict_match_rank

    assert strict_match_rank(registry_name, name) == rank


@pytest.mark.parametrize(
    "name,form",
    [("Czech Founders z.ú.", "zu"), ("Czech Founders VC s.r.o.", "sro"), ("Credo Ventures a.s.", "as"),
     ("KAYA,spol.s r.o.", "sro"), ("Reflex Capital SE", "se"), ("Look AI Ventures SICAV, a.s.", "as")],
)
def test_legal_form(name, form):
    assert legal_form(name) == form


def test_ticket_minimum_written_as_a_word_borrows_the_maximum_scale():
    # Jet Investment: "mezi jedním a dvěma miliony eur" -> min "jedním", max "dvěma miliony eur"
    lo, hi, flags = ticket_eur({"min": "jedním", "max": "dvěma miliony eur", "currency": "EUR"}, ON)
    assert (lo, hi, flags) == (1e6, 2e6, [])
