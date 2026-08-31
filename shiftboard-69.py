# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ShiftBoard
def reset_demo_data(db_path: str) -> None:
    """Reset ShiftBoard to demo state for manual testing."""
    from pathlib import Path
    from datetime import date

    db = Path(db_path)
    if not db.exists():
        db.parent.mkdir(parents=True, exist_ok=True)

    # Reset roles
    with open(db, "w") as f:
        f.write("Role,Name,Permissions\n")
        f.write("admin,admin,full_access\n")
        f.write("scheduler,scheduler,schedule_access\n")
        f.write("staff,staff,view_own_schedule\n")

    # Reset users
    with open(db, "w") as f:
        f.write("Username,Password,Role,Email\n")
        f.write("admin,admin123,admin,admin@shiftboard.com\n")
        f.write("scheduler,sched123,scheduler,scheduler@shiftboard.com\n")
        f.write("staff1,staff123,staff,staff1@shiftboard.com\n")
        f.write("staff2,staff223,staff,staff2@shiftboard.com\n")

    # Reset shifts
    with open(db, "w") as f:
        f.write("ShiftID,Start,End,Role,StaffID,Week,Notes\n")
        f.write("s1,2024-01-01,2024-01-01,staff,staff1,week1,\n")
        f.write("s2,2024-01-02,2024-01-02,staff,staff2,week1,\n")

    # Reset swaps
    with open(db, "w") as f:
        f.write("SwapID,StaffID,OriginalShift,ReplacementShift,Notes\n")
        f.write("swap1,staff1,s1,staff2,Test swap\n")

    # Reset availability
    with open(db, "w") as f:
        f.write("StaffID,Date,Available\n")
        f.write("staff1,2024-01-01,true\n")
        f.write("staff1,2024-01-02,true\n")
        f.write("staff2,2024-01-01,true\n")
        f.write("staff2,2024-01-02,true\n")

    # Reset rosters
    with open(db, "w") as f:
        f.write("Week,StaffID,Status\n")
        f.write("week1,staff1,assigned\n")
        f.write("week1,staff2,assigned\n")

    print(f"Demo data reset for {db_path}")
