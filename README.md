# ishkarim-misc

> **Eksperymenty i narzędzia — algorytmy, PoC, tematy przekrojowe**

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CPU-only](https://img.shields.io/badge/CPU-only-orange)]()

## Problem, który rozwiązujemy

- Repozytorium sprawdzonych pomysłów które nie pasują do głównych obszarów
- Algorytmy biologiczne/giełdowe z dokumentacją ograniczeń
- Małe narzędzia CLI do jednorazowych zadań

Pełna lista → [docs/PROBLEMS.md](docs/PROBLEMS.md)

## Szybki start

```bash
# Instalacja
pip install -e projects/ishkarim-misc

# Demo (10 sekund)
python projects/ishkarim-misc/demo.py
```

## Użycie w kodzie

```python
import ishkarim_misc as m

# Wszystkie 30 katalogi wiedzy obszaru 'misc'
docs = m.load_knowledge_index()
print(f"{len(docs)} katalogów | obszar: {m.__area__}")

# Narzędzia pomocnicze
from ishkarim_misc.utils import read_work_md, extract_tags, extract_python_blocks
```

## Dla kogo

- Inspiracja dla nowych projektów (sprawdź zanim wynajdujesz koło od nowa)
- Szybki prototyp do pokazania klientowi zanim podjęta decyzja
- Zbiór 'gotowców' — kopiuj fragmenty kodu do własnych projektów

## Dokumentacja

| Plik | Zawartość |
|------|-----------|
| [docs/PROBLEMS.md](docs/PROBLEMS.md) | Co rozwiązuje / czego nie / znane problemy |
| [docs/api.md](docs/api.md) | Dokumentacja API |
| [docs/overview.md](docs/overview.md) | Przegląd obszaru |
| [docs/sources.md](docs/sources.md) | Źródłowe katalogi wiedzy |
| [MODULES.md](MODULES.md) | Pełny indeks 30 katalogów |

## Testy i benchmarki

```bash
# Testy jednostkowe
pytest tests/test_misc.py -v

# Testy domenowe (z prawdziwymi danymi)
pytest tests/test_misc_domain.py -v

# Benchmarki wydajnościowe
python benchmarks/bench_misc.py --quick
```

## Struktura projektu

```
ishkarim-misc/
├── demo.py                    ← uruchom mnie
├── pyproject.toml
├── README.md
├── MODULES.md                 ← 30 katalogów-źródeł
├── docs/
│   ├── PROBLEMS.md            ← co rozwiązuje / czego nie
│   ├── api.md                 ← dokumentacja API
│   ├── overview.md
│   └── sources.md
├── src/ishkarim_misc/
│   ├── __init__.py            ← MODULES list + load_knowledge_index()
│   ├── utils.py               ← read_work_md, extract_tags, extract_python_blocks
│   └── snippets/              ← kod z WORK.md (referencyjny)
├── tests/
│   ├── test_misc.py         ← testy jednostkowe
│   └── test_misc_domain.py  ← testy domenowe
└── benchmarks/
    └── bench_misc.py        ← benchmarki wydajnościowe
```

## Ograniczenia

> ⚠️ To projekt **referencyjny** — wzorce i wiedza, nie gotowa biblioteka produkcyjna.
> Przed wdrożeniem produkcyjnym przeczytaj [docs/PROBLEMS.md](docs/PROBLEMS.md).

---

*Część ekosystemu [Ishkarim](../../README.md) — 30 katalogów wiedzy obszaru `misc`*
*Wygenerowano: 2026-03-11 | `scripts/build_projects.py` + `scripts/enrich_projects.py`*
