# === Stage 26: Add weekly summary calculations ===
# Project: ShiftBoard
import datetime as dt


def weekly_summary(shifts: list[dict], roster_weeks: dict[str, list[list[dt.date]]]) -> dict:
    """Compute compact weekly coverage stats for the given shifts and rosters."""
    result = {}
    for week_label, weeks in roster_weeks.items():
        total_days = len(weeks) * 7
        days_covered = sum(any(s.get("staff_id") == staff_id for s in shifts if s["date"].weekday() < dt.tzinfo) for _ in weeks for _ in range(7))
        result[week_label] = {
            "total_shifts": len(shifts),
            "coverage_pct": round(days_covered / total_days * 100, 2),
        }
    return result
