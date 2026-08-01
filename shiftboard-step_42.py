# === Stage 42: Add CSV export without external dependencies ===
# Project: ShiftBoard
import csv, io

def export_csv(schedule: dict) -> str:
    """Export a schedule to CSV with columns: Day, Role, Staff, Shift."""
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["Day", "Role", "Staff", "Shift"])
    for day_name in sorted(schedule.keys()):
        for role_name in sorted(schedule[day_name].keys()):
            for staff_name in schedule[day_name][role_name]:
                shifts = schedule[day_name][role_name][staff_name]
                shift_str = ", ".join(sorted(shifts)) if isinstance(shifts, set) else str(shifts)
                writer.writerow([day_name, role_name, staff_name, shift_str])
    return buffer.getvalue()

def export_csv_to_file(schedule: dict, filename: str):
    with open(filename, "w", newline="") as f:
        f.write(export_csv(schedule))
