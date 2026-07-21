# === Stage 11: Add JSON export for the current application state ===
# Project: ShiftBoard
import json, os

def export_state(roles, shifts):
    state = {
        "roles": [r.as_dict() for r in roles],
        "shifts": [s.as_dict() for s in shifts]
    }
    path = os.path.join(os.path.dirname(__file__), "state.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
    return state

def import_state(roles, shifts):
    path = os.path.join(os.path.dirname(__file__), "state.json")
    if not os.path.exists(path):
        raise FileNotFoundError("No saved state found.")
    with open(path, encoding="utf-8") as f:
        state = json.load(f)
    for r in state["roles"]:
        roles.append(Role(r["name"], r["role_type"]))
    for s in state["shifts"]:
        shifts.append(Shift(s["start_time"], s["end_time"], s["role_name"], s["staff_id"]))
