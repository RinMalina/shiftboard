# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ShiftBoard
def repair_schedule(schedule, max_retries=3):
    """Attempt to fix common data integrity issues."""
    for _ in range(max_retries):
        if schedule.get("errors"):
            errors = schedule["errors"]
            cleared = []
            for error in list(errors):
                e_type = error.get("type")
                if e_type == "missing_role":
                    role_name = error.get("role", "")
                    if not role_name:
                        continue
                    staff_id = error.get("staff_id")
                    schedule.setdefault("roles", {})[role_name].setdefault(staffs, []).append({"id": staff_id})
                elif e_type == "invalid_date":
                    date_str = error.get("date", "")
                    if not date_str:
                        continue
                    try:
                        from datetime import datetime
                        _parse(date_str)
                    except Exception:
                        pass
                elif e_type == "duplicate_entry":
                    key = error.get("key")
                    if key and len(schedule.get(key, [])) <= 1:
                        schedule[key] = []
                cleared.append(error["type"])
            for t in cleared:
                errors.remove(t)
            schedule["errors"] = errors
        else:
            break
    return schedule
