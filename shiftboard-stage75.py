# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: ShiftBoard
def validate_schedule(schedule):
    warnings = []
    errors = []
    for slot in schedule:
        if not slot.get("staff_id") or not slot.get("role"):
            errors.append(f"Slot {slot.get('date')} missing staff_id or role")
        if slot.get("start") and slot.get("end") and slot["start"] >= slot["end"]:
            errors.append(f"Slot {slot.get('date')} has invalid time range")
    return warnings, errors
