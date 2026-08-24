# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ShiftBoard
def _format_shift_table(table: dict, fmt: str) -> dict:
    """Return a copy of *table* with every value formatted by *fmt*."""
    return {k: fmt(v) for k, v in table.items()}


def _coverage_ratio(coverage: dict, total_slots: int) -> float:
    """Return the fraction of *total_slots* that have at least one worker."""
    return sum(1 for c in coverage.values() if c > 0) / total_slots


def _find_gaps(schedule: dict, min_gap: int) -> list:
    """Return list of (start, end) tuples where no worker is scheduled."""
    gaps = []
    for day in sorted(schedule):
        for slot in range(schedule[day][0], schedule[day][1]):
            if slot not in schedule[day]:
                gaps.append((day, slot))
    return gaps


def _nearest_shift(start: str, shifts: list) -> str:
    """Return the *shifts* entry whose start time is closest to *start*."""
    return min(shifts, key=lambda s: abs(s["start"] - start))


def _validate_shift(shift: dict, min_duration: int = 4) -> bool:
    """Return True if *shift* covers at least *min_duration* hours and has a name."""
    return bool(shift.get("name")) and (shift.get("end", 0) - shift.get("start", 0)) >= min_duration
