# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ShiftBoard
def dispatch(text):
    """Parse a simple text command and return (action, payload) tuple."""
    if not text:
        return ("noop", {})
    parts = text.strip().split(maxsplit=1)
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""
    if cmd == "help":
        return ("help", {"msg": "Available: help, add-role <name>, set-avail <weekday> <times>, swap <staffA> <staffB>, coverage, roster"})
    elif cmd == "add-role":
        return ("add_role", {"role_name": arg})
    elif cmd.startswith("set-avail"):
        rest = arg.split()
        if len(rest) >= 2:
            return ("set_availability", {"weekday": rest[0], "time_slot": rest[1]})
        return ("error", {"msg": f"Invalid set-avail command: {text}"})
    elif cmd == "swap":
        st = arg.split()
        if len(st) >= 2:
            return ("swap_shifts", {"staff_a": st[0], "staff_b": st[1]})
        return ("error", {"msg": f"Invalid swap command: {text}"})
    elif cmd == "coverage":
        return ("coverage_check", {})
    elif cmd == "roster":
        return ("show_roster", {})
    else:
        return ("error", {"msg": f"Unknown command: {cmd}"})
