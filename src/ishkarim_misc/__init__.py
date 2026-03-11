"""
ishkarim_misc — moduł z obszaru misc.

Różne: tematy niepasujące do głównych obszarów — algorytmy, narzędzia, eksperymenty.

Źródła: 30 katalogów z repozytorium Ishkarim.
"""
from __future__ import annotations

__version__ = "0.1.0"
__area__ = "misc"



MODULES: list[str] = [
    'Apple kupuje izraelski startup Q.ai za ok. 2 mld USD',
    'Bramki semantycznej spójności',
    'Brytyjski regulator chce „AI opt‑out” dla wydawców_04',
    'Building Systems That Learn from Errors',
    'Dlaczego produkcja chipów na Tajwanie ma znaczenie_04',
    'Dokumentacja produktu',
    'Dwuminutowe porządki w notatkach z pomysłami',
    'Fresh experimental AI projects surfaced',
    'Jak odzyskać rytm po zmianach w aplikacjach',
    'Jak wykorzystać 15‑minutową lukę w kalendarzu',
    'Kiedy HISM wygrywa z aktorami w budynkach',
    'Kolumna ‘Verified’ po ‘Done’',
    'MVP przeglądarki instrukcja',
    'Microsoft załatał lukę zero‑day w\u202fOffice',
    'Nowości w Pythonie 3.14',
    'Nowy telefon Galaxy z funkcjami AI',
    'Offline demo wiedza połączona z 3D wizualizacją_04',
    'Offline’owy łańcuch narzędzi: Knuth–Plass i\u202fhyphenacja',
    'OpenAI wycofuje starsze modele 13 lutego',
    'Presja wydatków na AI w big techu',
    'Prototyp bramki spójności semantycznej',
    'Python - testy doctest i snapshoty z Markdown',
    'R3DAP',
    'Rytm przepływu sekcji',
    'Samodzielny audyt ewolucji instrukcji AI',
    'Semantyczne bramki jakości dla wyników AI',
    'Tematy poboczne',
    'YAML front‑matter jako API dokumentacji',
    'Zastosowania języka ADA',
    'Zmiany w API OpenAI: ważne terminy 2026',
]


_REPO_ROOT: str | None = None


def _find_repo_root() -> str:
    """Auto-discover the Ishkarim repo root by walking up from __file__."""
    from pathlib import Path
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "CATALOG.md").exists() or (p / "CHANGELOG.md").exists():
            return str(p)
        p = p.parent
    return str(Path(__file__).resolve().parents[5])  # fallback


def load_knowledge_index(root: str | None = None) -> list[dict]:
    """
    Zwraca listę rekordów ze wszystkich katalogów-źródeł obszaru.

    Args:
        root: ścieżka do katalogu głównego repozytorium (opcjonalne)

    Returns:
        Lista słowników z kluczami: name, doc_id, maturity, area
    """
    import re
    from pathlib import Path

    if root is None:
        root = _find_repo_root()

    results = []
    for name in MODULES:
        tags_path = Path(root) / name / "TAGS.md"
        if not tags_path.exists():
            continue
        tags = tags_path.read_text(errors="replace")
        doc_id = ""
        maturity = "draft"
        m = re.search(r"^doc_id:\s*(\S+)", tags, re.M)
        if m:
            doc_id = m.group(1)
        m2 = re.search(r"^maturity:\s*(\S+)", tags, re.M)
        if m2:
            maturity = m2.group(1)
        results.append({"name": name, "doc_id": doc_id, "maturity": maturity, "area": "misc"})
    return results


__all__ = ["MODULES", "load_knowledge_index", "__version__", "__area__"]
