from investordb.report import overall


def test_overall_verdict_from_primary_questions():
    yes = {"real_investor": "yes", "active_36m": "yes", "type_vc": "yes", "hq_cz_sk": "yes"}
    assert overall(yes) == "include"
    assert overall({**yes, "active_36m": "no"}) == "exclude"
    assert overall({**yes, "hq_cz_sk": "cannot_tell"}) == "cannot_tell"
    # a single "no" decides even when other answers are unknown
    assert overall({"real_investor": "no", "active_36m": "cannot_tell"}) == "exclude"
