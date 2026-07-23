# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ShiftBoard
def dry_run(self, command):
    """Simulate a state-mutating command without applying it."""
    if command not in self._dry_commands:
        raise ValueError(f"Unknown dry-run command: {command}")
    sim = ShiftBoard.__new__(ShiftBoard)
    sim.role_names = list(self.role_names)
    sim.staff_availability = dict(self.staff_availability)
    sim.shift_assignments = dict(self.shift_assignments)
    sim.swaps = list(self.swaps)
    sim.weekly_rosters = list(self.weekly_rosters)
    sim.config = dict(self.config)
    if command == 'assign':
        _, staff, shift, slot = self._parse_assign_input()
        if (staff in sim.staff_availability and
            not any(slot in v.get(shift, []) for v in sim.staff_availability.values())):
            sim.shift_assignments[(staff, shift)] = slot
    elif command == 'swap':
        _, staff1, role1, date1, slot1, staff2, role2, date2, slot2 = self._parse_swap_input()
        if (role1 in sim.role_names and role2 in sim.role_names):
            for s in [staff1, staff2]:
                if s not in sim.staff_availability:
                    raise ValueError(f"Staff {s} not in availability")
                if date1 not in sim.staff_availability[staff1] or date2 not in sim.staff_availability[staff2]:
                    raise ValueError("Date not available for one of the staff members")
            sim.swaps.append({
                'staff1': staff1, 'role1': role1, 'date1': date1, 'slot1': slot1,
                'staff2': staff2, 'role2': role2, 'date2': date2, 'slot2': slot2,
            })
    elif command == 'remove':
        _, staff = self._parse_remove_input()
        if (staff in sim.shift_assignments and
            any(slot not in v.get(shift, []) for v in sim.staff_availability.values())):
            del sim.shift_assignments[(staff, shift)]
    return sim
