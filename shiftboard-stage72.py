# === Stage 72: Add Markdown report export ===
# Project: ShiftBoard
def export_markdown_report(db_path, report_path):
    """Export a compact Markdown summary of the ShiftBoard database."""
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    roles = [r[0] for r in cur.execute("SELECT name FROM roles ORDER BY name")]
    shifts = [r[0] for r in cur.execute("SELECT name FROM shifts ORDER BY name")]
    staff = [r[0] for r in cur.execute("SELECT name FROM staff ORDER BY name")]
    coverage = cur.execute("SELECT COUNT(*) FROM coverage WHERE assigned = 1").fetchone()[0]
    total = cur.execute("SELECT COUNT(*) FROM coverage").fetchone()[0]
    coverage_pct = f"{coverage / total * 100:.0f}%" if total else "N/A"

    lines = [
        "# ShiftBoard Report",
        "",
        f"- **Staff**: {len(staff)}",
        f"- **Roles**: {len(roles)}",
        f"- **Shifts**: {len(shifts)}",
        f"- **Coverage**: {coverage_pct}",
        "",
        "## Roles",
    ]
    for r in roles:
        lines.append(f"- {r}")
    lines.append("")
    lines.append("## Shifts")
    for s in shifts:
        lines.append(f"- {s}")
    lines.append("")
    lines.append("## Staff")
    for s in staff:
        lines.append(f"- {s}")

    with open(report_path, "w") as f:
        f.write("\n".join(lines))
