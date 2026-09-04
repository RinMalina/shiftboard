# === Stage 81: Add final README text as a module string with usage examples ===
# Project: ShiftBoard
def usage_example():
    """
    ShiftBoard — a staff shift scheduler with roles, availability, swaps,
    coverage checks, and weekly rosters.

    Usage:
        from shiftboard import ShiftBoard

        board = ShiftBoard("Nursing")
        board.add_staff("Alice", ["Mon", "Tue", "Wed"])
        board.add_staff("Bob",   ["Tue", "Wed", "Thu"])
        board.add_staff("Carol", ["Mon", "Wed", "Fri"])
        board.add_role("Nurse")
        board.add_role("Assistant")

        # Schedule shifts
        board.schedule("Alice", "Nurse", "Mon", "08:00", "16:00")
        board.schedule("Bob",   "Nurse", "Tue", "08:00", "16:00")
        board.schedule("Carol", "Assistant", "Wed", "08:00", "16:00")

        # Swap shifts
        board.swap_shift("Alice", "Bob", "Mon")

        # Check coverage
        coverage = board.check_coverage("Mon")
        print(f"Monday coverage: {coverage}")

        # Generate weekly roster
        roster = board.generate_roster()
        print(roster)
    """
    pass
