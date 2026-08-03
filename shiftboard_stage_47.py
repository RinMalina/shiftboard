# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ShiftBoard
def demo():
    roles = ['barista', 'cook', 'cashier']
    staff  = [Staff(name='Anna'), Staff(name='Ben'), Staff(name='Clara')]
    for s in staff: s.role = roles.pop() if len(roles) else 'barista'

    shifts = {
        '2024-12-09': {'morning': 3, 'afternoon': 2},
        '2024-12-16': {'morning': 3, 'afternoon': 2},
    }
    schedule = Schedule(shifts)

    for s in staff:
        avail = Availability(s.name, ['mon','wed','fri'], ['morning','afternoon'])
        schedule.add_staff_availability(avail)

    swapper = Swapper(schedule)
    swapper.request_swap(Staff('Anna'), '2024-12-09', 'morning')
    print(swapper.status())          # → pending / confirmed

    checker = CoverageChecker(schedule, min_per_role={'barista': 1})
    print(checker.report('2024-12-09'))   # → coverage OK or short

    roster = WeeklyRoster(schedule)
    roster.build(roles, staff)
    print(roster.display())
