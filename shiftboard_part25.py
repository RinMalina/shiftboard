# === Stage 25: Add daily summary calculations ===
# Project: ShiftBoard
def daily_summary(shifts, roles):
    """Return a dict with per-role counts and total shifts for each day."""
    summary = {}
    for role in roles:
        summary[role] = 0
    if not shifts:
        return summary
    for shift in shifts:
        role_name = shift.get("role") or "unassigned"
        summary[role_name] = summary.get(role_name, 0) + 1
        total_key = f"total_{role_name}"
        summary[total_key] = summary.get(total_key, 0) + 1
    return summary
