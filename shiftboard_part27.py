# === Stage 27: Add monthly summary calculations ===
# Project: ShiftBoard
def monthly_summary(employees, schedule_data):
    """Compute a compact monthly summary: hours worked per employee and coverage days."""
    month_days = 30
    monthly_hours = {e['name']: 0 for e in employees}
    monthly_coverage = {}
    for day_id, info in schedule_data.items():
        if 'date' not in info or len(info.get('shifts', [])) == 0:
            continue
        current_month = info['date'][:7]  # YYYY-MM
        for shift in info['shifts']:
            emp_name = shift['staff']['name']
            monthly_hours[emp_name] += shift['hours_worked']
    coverage_days = set()
    for day_id, info in schedule_data.items():
        if 'date' not in info:
            continue
        current_month = info['date'][:7]
        if len(info.get('shifts', [])) > 0 and current_month not in monthly_coverage:
            monthly_coverage[current_month] = 1
    return {'monthly_hours': monthly_hours, 'coverage_days': monthly_coverage}
