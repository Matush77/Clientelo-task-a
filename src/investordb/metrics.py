"""Statistics behind the pre-registered metrics in docs/PLAN.md (chapter 9)."""

from __future__ import annotations

import math


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float, float]:
    """Proportion k/n with its Wilson score interval (better than the normal approximation for small n or p near 1)."""
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    margin = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return p, max(0.0, center - margin), min(1.0, center + margin)


def cohen_kappa(a: list[str], b: list[str]) -> float:
    """Agreement between two raters beyond chance (1 = perfect, 0 = chance level)."""
    if len(a) != len(b) or not a:
        raise ValueError("need two equally long, non-empty rating lists")
    n = len(a)
    labels = set(a) | set(b)
    observed = sum(x == y for x, y in zip(a, b)) / n
    expected = sum((a.count(l) / n) * (b.count(l) / n) for l in labels)
    return 1.0 if expected == 1 else (observed - expected) / (1 - expected)


def chapman(n_a: int, n_b: int, m: int) -> tuple[float, float, float]:
    """Capture-recapture estimate of population size from two lists (Chapman's bias-corrected Lincoln-Petersen).

    n_a, n_b = verified investors found by list A / list B, m = found by both. Returns (N, 95% CI low, high).
    Assumes the lists are independent; both favour visible investors, so N is a lower bound.
    """
    n = (n_a + 1) * (n_b + 1) / (m + 1) - 1
    var = (n_a + 1) * (n_b + 1) * (n_a - m) * (n_b - m) / ((m + 1) ** 2 * (m + 2))
    se = math.sqrt(var)
    seen = n_a + n_b - m
    return n, max(seen, n - 1.96 * se), n + 1.96 * se


def sample_size(p: float, margin: float, z: float = 1.96) -> int:
    """Records to check by hand so that precision p is known to +-margin (used in the cost model)."""
    return math.ceil(z * z * p * (1 - p) / (margin * margin))
