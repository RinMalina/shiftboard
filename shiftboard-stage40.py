# === Stage 40: Add plain text report export ===
# Project: ShiftBoard
def export_report_to_text(teams, shifts):
    """Export a plain-text shift report."""
    lines = []
    for t in teams:
        lines.append(f"Team: {t['name']}\n")
        for sh in shifts:
            if sh.get("team_id") == t["id"]:
                assigned = sh.get("assigned_to", "unassigned")
                role = sh.get("role_name", "")
                date = sh.get("date", "")
                lines.append(f"  {date} | {role:<15} | {assigned}")
        lines.append("\n")
    return "\n".join(lines)
