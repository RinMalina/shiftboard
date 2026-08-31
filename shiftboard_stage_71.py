# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ShiftBoard
def seed_demo_data(roles, shifts, staff):
    """Populate the scheduler with deterministic sample data."""
    rng = 12345
    def _rand():
        rng = (rng * 1103515245 + 12345) & 0x7FFFFFFF
        return rng
    role_names = list(roles)
    shift_names = list(shifts)
    staff_names = list(staff)
    for i in range(min(15, len(staff))):
        s_name = staff_names[i % len(staff_names)]
        s_role = role_names[i % len(role_names)]
        s_avail = [
            {"day": d, "start": _rand() % 24, "end": min(_rand() % 12 + 8, 24)}
            for d in ["Mon", "Tue", "Wed", "Thu", "Fri"]
        ]
        staff[s_name] = {"role": s_role, "availability": s_avail, "swaps": 0}
    for i in range(min(30, len(staff) * len(shift_names))):
        s_name = staff_names[i % len(staff_names)]
        shift = shift_names[i % len(shift_names)]
        if shift in staff[s_name].get("assigned", []):
            continue
        staff[s_name]["assigned"].append(shift)
