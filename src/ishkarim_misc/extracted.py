"""
extracted.py — kod wyekstrahowany z WORK.md dla obszaru misc.

Zawiera 5 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: Dlaczego produkcja chipów na Tajwanie ma znaczenie_04
@dataclass
class SwitchTime:
    redesign_m: float; tapeout_m: float; process_qual_m: float
    packaging_qual_m: float; contract_m: float; logistics_m: float

def risk_score(p: RiskParams) -> float:
    base = (p.supplier_concentration * (1.0 + p.switch_time_months/12.0)) * (p.criticality/5.0)
    return base * (1.0 + 0.5 * p.allocation_pressure)

# Source: Dlaczego produkcja chipów na Tajwanie ma znaczenie_04
def edmonds_karp(cap, s, t): ...
def min_cut_edges(original_cap, residual_cap, s): ...
def deliverable_for_product(model, product_id): ...  # max-flow per flow + Leontief

# Source: Nowy telefon Galaxy z funkcjami AI
@dataclass
class Ctx:
    task: str; context_chars: int; offline: bool; metered: bool
    battery_pct: int; thermal_state: str; sensitivity: str
    user_cloud_opt_in: bool; org_cloud_allowed: bool

def route(ctx: Ctx) -> tuple[Route, list[str]]:
    if ctx.offline: return (Route.LOCAL_FALLBACK, ["OFFLINE"])
    if ctx.sensitivity in {"finance", "enterprise"}:
        if not ctx.user_cloud_opt_in or not ctx.org_cloud_allowed:
            return (Route.LOCAL, ["SENSITIVE_BLOCK_CLOUD"])
    if ctx.thermal_state == "hot" or ctx.battery_pct < 15:
        return (Route.CLOUD, ["RESOURCE_PRESSURE_USE_CLOUD"])
    if ctx.context_chars > 12000 and ctx.user_cloud_opt_in:
        return (Route.CLOUD, ["CONTEXT_TOO_LARGE_FOR_LOCAL"])
    return (Route.LOCAL, ["DEFAULT_LOCAL"])

# Source: Nowy telefon Galaxy z funkcjami AI
@dataclass
class TaskRun:
    task_id: str; baseline_steps: int; baseline_seconds: float
    ai_steps: int; ai_seconds: float; ai_errors: int; ai_manual_edits: int

# Source: Tematy poboczne
# Pętla percepcyjna 100ms
while True:
    feat = fuse(
      read("SELECT rms FROM last3s_audio ORDER BY ts DESC LIMIT 30"),
      read("SELECT motion FROM last3s_video ORDER BY ts DESC LIMIT 15")
    )
    y = model.predict(feat)
    if y["alert"] > 0.8:
        emit_event("motion_alert", y["alert"], {...})
    sleep(0.1)
