# === Stage 67: Add a function that returns key project metrics ===
# Project: ShiftBoard
def get_project_metrics():
    """Return key ShiftBoard metrics."""
    return {
        "version": "1.0.0",
        "features": {
            "roles": True,
            "availability": True,
            "swaps": True,
            "coverage_check": True,
            "weekly_roster": True,
        },
        "total_roles": 5,
        "max_shifts_per_day": 3,
        "shift_hours": {"morning": 4, "afternoon": 4, "night": 4},
        "coverage_target": 0.95,
        "swap_limit": 2,
        "roster_days": 7,
        "dependencies": [],
    }
