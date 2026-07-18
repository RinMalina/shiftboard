# === Stage 4: Implement create operations for the primary records ===
# Project: ShiftBoard
def create_shifts(employees, roles, availability):
    shifts = []
    for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
        morning = {"start": 8, "end": 12}
        evening = {"start": 16, "end": 20}
        for slot in (morning, evening):
            for emp in employees:
                if emp["role"] == roles[day]["required_role"]:
                    if emp["name"] in availability.get(day, []):
                        shifts.append({
                            "id": len(shifts) + 1,
                            "employee_name": emp["name"],
                            "employee_id": emp["id"],
                            "role": emp["role"],
                            "day": day,
                            "slot": slot,
                            "start_time": slot["start"],
                            "end_time": slot["end"]
                        })
    return shifts

def create_swap(requester_id, shift_date, original_employee_name, replacement_employee_name):
    swap = {
        "id": len(SWAPS) + 1 if SWAPS else 1,
        "requester_id": requester_id,
        "shift_date": shift_date,
        "original_employee_name": original_employee_name,
        "replacement_employee_name": replacement_employee_name,
        "status": "pending"
    }
    SWAPS.append(swap)

def create_coverage_report(employees, roles):
    report = {"date": "Weekly", "coverage": {}, "gaps": []}
    for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
        required = roles[day]["required_count"]
        available = len([e for e in employees if e["role"] == roles[day]["required_role"]])
        report["coverage"][day] = {"required": required, "available": available}
        if available < required:
            report["gaps"].append({"day": day, "shortage": required - available})
    return report

def create_weekly_roster(employees, roles):
    roster = []
    for emp in employees:
        schedule = {"employee_name": emp["name"], "employee_id": emp["id"], "role": emp["role"]}
        for day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
            if emp["role"] == roles[day]["required_role"]:
                schedule[day] = True
        roster.append(schedule)
    return roster
