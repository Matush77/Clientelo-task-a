import pytest

from investordb.triage import registry_name_matches


@pytest.mark.parametrize(
    "registry_name,brand",
    [
        ("Credo Ventures a.s.", "Credo Ventures"),
        ("Reflex Capital Partners s.r.o.", "Reflex Capital"),
        ("Nation1 Investment s.r.o.", "Nation1"),  # one-word brand + investment word only
        ("DEPO VENTURES, s.r.o.", "DEPO VENTURES s.r.o."),
        ("ZAKA VC I, osoba rizikového kapitálu, a.s.", "ZAKA Ventures"),  # entity shorter than the brand
        ("J&T Ventures CG SICAV a.s.", "J&T Ventures"),
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
        ("ZAKA REKONSTRUKCE s.r.o.", "ZAKA Ventures"),
        ("MITON Circus a.s.", "Miton"),
        # regressions: one-word company names that merely share a VC's brand (false matches in the first run)
        ("KAYA,spol.s r.o.", "KAYA"),
        ("ZAKA, s.r.o.", "ZAKA Ventures"),
        ("MITON One s.r.o.", "Miton"),
    ],
)
def test_registry_name_mismatches(registry_name, brand):
    assert not registry_name_matches(registry_name, brand)
