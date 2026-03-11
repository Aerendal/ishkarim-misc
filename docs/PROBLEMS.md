# PROBLEMS — ishkarim-misc

> Eksperymenty i narzędzia — algorytmy, PoC, tematy przekrojowe

## ✅ Co ten projekt rozwiązuje

- ✅ Repozytorium sprawdzonych pomysłów które nie pasują do głównych obszarów
- ✅ Algorytmy biologiczne/giełdowe z dokumentacją ograniczeń
- ✅ Małe narzędzia CLI do jednorazowych zadań
- ✅ PoC przed decyzją o inwestycji w pełny moduł

---

## ❌ Czego ten projekt NIE rozwiązuje

- ❌ Spójny obszar tematyczny — celowo heterogeniczny zbiór
- ❌ Produkcyjne implementacje — eksperymenty i prototypy
- ❌ Długoterminowe utrzymanie — może być nieaktualne

---

## ⚠️ Znane problemy i ograniczenia

- ⚠️ **Brak spójnych konwencji** między katalogami — różne style kodu
- ⚠️ **Niektóre PoC** zależą od zewnętrznych API które mogły się zmienić
- ⚠️ **Dokumentacja minimalna** — WORK.md pisane jako notatki, nie tutorial

---

## 🎯 Przypadki użycia

- 🎯 Inspiracja dla nowych projektów (sprawdź zanim wynajdujesz koło od nowa)
- 🎯 Szybki prototyp do pokazania klientowi zanim podjęta decyzja
- 🎯 Zbiór 'gotowców' — kopiuj fragmenty kodu do własnych projektów

---

## 📊 Matryca decyzyjna

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy potrzebujesz GPU? | **NIE** — zaprojektowany dla CPU-only |
| Czy działa offline? | **TAK** — zero zewnętrznych zależności sieciowych |
| Czy jest produkcyjny? | **WZORCE** — referencja do implementacji, nie plug-and-play |
| Czy obsługuje skalowanie? | **LOKALNIE** — single-node, do ~kilku tysięcy dokumentów |
| Licencja? | **MIT** — możesz używać w projektach komercyjnych |

---

## 🔗 Powiązane projekty

Inne moduły Ishkarim które uzupełniają ten projekt:

| Projekt | Relacja |
|---------|---------|
| `ishkarim-rag` | Wyszukiwanie semantyczne nad bazą wiedzy |
| `ishkarim-sqlite` | Trwała pamięć i event-sourcing |
| `ishkarim-agent` | Architektura agentów AI |
| `ishkarim-security` | Bezpieczeństwo systemów AI |
| `ishkarim-bench` | Benchmarki wydajnościowe |

---

*Ostatnia aktualizacja: 2026-03-11 | Generator: `scripts/enrich_projects.py`*
