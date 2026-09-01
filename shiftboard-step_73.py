# === Stage 73: Add a lightweight HTML report export ===
# Project: ShiftBoard
class HTMLReport:
    def __init__(self, staff, shifts, swaps, coverage):
        self.staff = staff
        self.shifts = shifts
        self.swaps = swaps
        self.coverage = coverage

    def generate(self):
        lines = ['<html><head><style>table{border-collapse:collapse}td,th{border:1px solid #ddd;padding:6px;text-align:left}</style></head><body>']
        lines.append('<h1>ShiftBoard Weekly Report</h1>')
        lines.append('<h2>Staff Roster</h2><table><tr><th>Name</th><th>Role</th><th>Shifts Assigned</th><th>Coverage</th></tr>')
        for s in self.staff:
            lines.append(f'<tr><td>{s.name}</td><td>{s.role}</td><td>{len(s.shifts)}</td><td>{s.coverage_pct}%</td></tr>')
        lines.append('</table>')
        lines.append('<h2>Swap Log</h2><ul>')
        for sw in self.swaps:
            lines.append(f'<li>{sw.from_staff} <-> {sw.to_staff} on {sw.date}</li>')
        lines.append('</ul>')
        lines.append('</body></html>')
        return '\n'.join(lines)
