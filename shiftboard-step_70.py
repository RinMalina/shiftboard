# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ShiftBoard
def clear_state():
    """Reset all internal ShiftBoard data structures to their initial values."""
    global _staff, _roles, _availability, _swaps, _roster, _coverage, _confirm_flag

    _staff = {}
    _roles = {}
    _availability = {}
    _swaps = {}
    _roster = {}
    _coverage = {}
    _confirm_flag = True

    if not _confirm_flag:
        raise PermissionError("Confirmation flag is disabled; cannot clear state.")

    print("\n✅ State cleared successfully.")
