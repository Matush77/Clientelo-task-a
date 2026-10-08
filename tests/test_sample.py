from collections import Counter

from investordb.sample import draw


def decisions(n_included):
    rows = [{"candidate_id": f"I{i:03d}", "status": "INCLUDED"} for i in range(n_included)]
    rows += [{"candidate_id": f"R{i:03d}", "status": "REJECTED"} for i in range(20)]
    rows += [{"candidate_id": f"K{i:03d}", "status": "REJECTED"} for i in range(12)]
    rows += [{"candidate_id": "C012", "status": "INCLUDED"}]  # calibration record - must never be sampled
    return rows


CONTROLS = {f"K{i:03d}" for i in range(12)}


def test_strata_sizes_and_calibration_excluded():
    picked = draw(decisions(60), CONTROLS)
    assert Counter(s for s, _ in picked) == {"included": 30, "real_reject": 5, "control_reject": 5}
    assert "C012" not in {d["candidate_id"] for _, d in picked}


def test_small_included_set_becomes_census():
    picked = draw(decisions(33), CONTROLS)
    assert Counter(s for s, _ in picked)["included"] == 33


def test_draw_is_deterministic():
    ids = lambda: [d["candidate_id"] for _, d in draw(decisions(60), CONTROLS)]
    assert ids() == ids()
