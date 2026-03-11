# ishkarim-misc

> Różne: tematy niepasujące do głównych obszarów — algorytmy, narzędzia, eksperymenty.

## Instalacja

```bash
pip install -e projects/ishkarim-misc
```

Lub lokalnie z tego repozytorium:

```bash
cd projects/ishkarim-misc
pip install -e ".[dev]"
```

## Użycie

```python
import ishkarim_misc as m

# Lista dostępnych modułów
print(m.MODULES)

# Wczytaj indeks wiedzy
docs = m.load_knowledge_index()
```

## Obszar tematyczny

Ten projekt agreguje wiedzę z **30 katalogów** obszaru `misc`:

- `Apple kupuje izraelski startup Q.ai za ok. 2 mld USD`
- `Bramki semantycznej spójności`
- `Brytyjski regulator chce „AI opt‑out” dla wydawców_04`
- `Building Systems That Learn from Errors`
- `Dlaczego produkcja chipów na Tajwanie ma znaczenie_04`
- `Dokumentacja produktu`
- `Dwuminutowe porządki w notatkach z pomysłami`
- `Fresh experimental AI projects surfaced`
- … i 22 więcej (pełna lista w [MODULES.md](MODULES.md))

## Przykładowe źródła

### Apple kupuje izraelski startup Q.ai za ok. 2 mld USD

# Apple kupuje izraelski startup Q.ai za ok. 2 mld USD
## 0-Metadane
- Pliki: 1
- Tagi: Apple, akwizycja, Q.ai, silent-speech, audio-AI, AirPods, Vision-Pro, Siri, izrael, stealth-startup
- Status: done

### Bramki semantycznej spójności

# WORK — Bramki semantycznej spójności
> Notatki robocze z deep-index. Ostatnia aktualizacja: 2026-02-25.
---
## 0. Metadane
- **Katalog:** Bramki semantycznej spójności

### Brytyjski regulator chce „AI opt‑out” dla wydawców_04

# WORK: Brytyjski regulator chce „AI opt‑out” dla wydawców_04
## 0-Metadane
- Katalog: Brytyjski regulator chce „AI opt‑out” dla wydawców_04
- Pliki: 13 (z treścią >120 B); łącznie 15
- Tagi: regulacje, AI-prawo, CMA, Google, wydawcy, compliance, opt-out


## Struktura projektu

```
ishkarim-misc/
├── pyproject.toml        # installable package
├── README.md
├── MODULES.md            # pełny indeks 30 katalogów-źródeł
├── src/
│   └── ishkarim_misc/
│       ├── __init__.py   # publiczne API
│       ├── utils.py      # wspólne narzędzia
│       └── *.py          # kod wyekstrahowany z WORK.md
├── tests/
│   ├── __init__.py
│   └── test_misc.py
└── docs/
    ├── overview.md
    └── sources.md
```

## Testy

```bash
pytest projects/ishkarim-misc/tests/ -v
```

## Źródło danych

Katalogi źródłowe znajdują się w katalogu głównym repozytorium Ishkarim.
Każdy katalog zawiera `WORK.md` (notatki badawcze) i `TAGS.md` (metadane).

---
*Wygenerowano automatycznie przez `scripts/build_projects.py`*
