# === Stage 37: Add recommendations for the next useful action ===
# Project: ShiftBoard
def suggest_next_actions(week_rosters, coverage_gaps):
    suggestions = []
    for day, gaps in coverage_gaps.items():
        if gaps:
            missing_roles = list(set(r for _, r in gaps))
            available_staff = [s for s in week_rosters.values() if s['status'] == 'available']
            for role in missing_roles:
                candidates = [s for s in available_staff if any(role in a.get('roles', []) for a in s.get('availability', {}).values())]
                if candidates:
                    suggestions.append(f"Assign {role} on {day} from one of: {[c['name'] for c in candidates]}")
    return suggestions
