import pytest

from investordb.candidates import match_key, same_entity


@pytest.mark.parametrize(
    "a,b",
    [
        ("Credo Ventures", "Credo Ventures a.s."),
        ("Neulogy Ventures", "Neulogy Ventures, a. s."),
        ("DEPO Ventures", "DEPO Ventures One SCSp"),
        ("KAYA VC", "Kaya"),
        ("Nation1", "Nation 1"),
        ("Tilia Impact Ventures – Čestný člen", "Tilia Impact Ventures"),
    ],
)
def test_same_entity(a, b):
    assert same_entity(match_key(a), match_key(b))


@pytest.mark.parametrize(
    "a,b",
    [
        ("Innova Capital", "Inovia Capital"),  # Polish PE vs Canadian VC - found as a false merge in the first run
        ("J&T Ventures", "Jet Ventures"),
        ("Venture to Future Fund", "Future Fund"),
        ("Genesis Capital", "Genesis Ventures"),
    ],
)
def test_different_entities(a, b):
    assert not same_entity(match_key(a), match_key(b))
