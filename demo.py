#!/usr/bin/env python3
"""
demo.py — demo ishkarim-misc

Eksperymenty i narzędzia — algorytmy, PoC, tematy przekrojowe

Uruchomienie:
    python projects/ishkarim-misc/demo.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[0] / "src"))
import ishkarim_misc as m
from ishkarim_misc.utils import extract_tags

docs = m.load_knowledge_index()
root = pathlib.Path(__file__).parents[2]

print(f"Misc/Eksperymenty — {len(docs)} katalogów wiedzy\n")
by_mat = {}
for d in docs:
    by_mat.setdefault(d["maturity"], []).append(d)
for mat, items in sorted(by_mat.items()):
    print(f"  {mat:12s}: {len(items):2d} katalogów")
print()
print("Przykłady:")
for d in docs[:5]:
    print(f"  • {d['name'][:70]}")

