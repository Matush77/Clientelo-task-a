import pytest

from investordb.metrics import chapman, cohen_kappa, sample_size, wilson


@pytest.mark.parametrize(
    "k,n,lo,hi",
    [(30, 30, 0.886, 1.0), (27, 30, 0.744, 0.965), (10, 10, 0.722, 1.0), (0, 10, 0.0, 0.278)],
)
def test_wilson_known_values(k, n, lo, hi):
    _, low, high = wilson(k, n)
    assert low == pytest.approx(lo, abs=0.001)
    assert high == pytest.approx(hi, abs=0.001)


def test_kappa():
    assert cohen_kappa(["in", "out", "in", "out"], ["in", "out", "in", "out"]) == 1.0
    # 80 % raw agreement, but both raters say "in" most of the time -> kappa much lower
    a = ["in"] * 8 + ["out"] * 2
    b = ["in"] * 7 + ["out"] + ["in"] + ["out"]
    assert cohen_kappa(a, b) == pytest.approx(0.375, abs=0.001)


def test_chapman():
    n, lo, hi = chapman(40, 20, 10)
    assert n == pytest.approx(77.27, abs=0.01)
    assert lo >= 50  # never below the number actually seen (40 + 20 - 10)
    assert hi > n


def test_sample_size_for_cost_model():
    assert sample_size(0.9, 0.05) == 139
