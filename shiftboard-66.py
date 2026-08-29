# === Stage 66: Add export of a short status dashboard ===
# Project: ShiftBoard
def export_dashboard(employees, roles, schedules, swaps):
    dashboard = {"status": "ShiftBoard", "date": today(), "coverage": [], "swaps_pending": []}
    for role in roles:
        available = [e for e in employees if role in e["roles"]]
        scheduled = [e for e in available if role in e["schedule"].get("today", {})]
        dashboard["coverage"].append({"role": role, "available": len(available), "scheduled": len(scheduled)})
    dashboard["swaps_pending"] = len(swaps)
    return dashboard
