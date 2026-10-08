import pytest

from investordb.triage import registry_name_matches


@pytest.mark.parametrize(
    "registry_name,brand",
    [
        ("Credo Ventures a.s.", "Credo Ventures"),
        ("Reflex Capital Partners s.r.o.", "Reflex Capital"),
        ("Nation1 Investment s.r.o.", "Nation1"),  # one-word brand + investment word only
        ("DEPO VENTURES, s.r.o.", "DEPO VENTURES s.r.o."),
    ],
)
def test_registry_name_matches(registry_name, brand):
    assert registry_name_matches(registry_name, brand)


@pytest.mark.parametrize(
    "registry_name,brand",
    [
        ("KAYA CONSTRUCTION s.r.o.", "KAYA"),  # one-word brand + unrelated word: a different company
        ("Mehmet Salih Kaya", "KAYA"),
        ("Inovia Capital s.r.o.", "Innova Capital"),
    ],
)
def test_registry_name_mismatches(registry_name, brand):
    assert not registry_name_matches(registry_name, brand)
