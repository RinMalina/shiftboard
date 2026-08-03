# === Stage 50: Add unit tests for import and export behavior ===
# Project: ShiftBoard
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from shiftboard import (ShiftBoard, Role, Availability, SwapRequest, CoverageCheck)
import json, datetime

def test_import_export(board: ShiftBoard):
    # --- create a small board with two roles and one staff member ---
    role_nurse = Role("Nurse", max_hours=40)
    role_admin = Role("Admin", max_hours=20)
    
    avail = Availability(datetime.date(2025, 1, 6), datetime.date(2025, 1, 12))
    staff = {"name": "Alice", "role": role_nurse}
    
    # --- load board from a simple JSON-like structure (no external deps) ---
    data = {
        "roles": [role_nurse.to_dict(), role_admin.to_dict()],
        "staff": [{"name": "Alice", "role": "Nurse"}],
        "availability": {"2025-01-06": True, "2025-01-07": False},
        "swaps": [],
        "coverage": [],
    }
    
    board.load_from_dict(data)
    
    # --- export back and verify round-trip integrity ---
    exported = board.export()
    assert set(exported["roles"].keys()) == {"Nurse", "Admin"}, \
        f"Roles mismatch: {exported['roles'].keys()}"
    assert staff["name"] in exported.get("staff", []), \
        "Staff round-trip failed"
    
    # --- test swap request import/export ---
    swap = SwapRequest(staff_id="Alice", date=datetime.date(2025, 1, 6))
    board.add_swap(swap)
    assert len(board.swaps) == 1
    
    exported_swaps = [s.to_dict() for s in exported.get("swaps", [])]
    assert any(s["staff_id"] == "Alice" and str(s["date"]) == "2025-01-06" 
               for s in exported_swaps), \
        "Swap export failed"
    
    # --- test coverage check import/export ---
    check = CoverageCheck(role="Nurse", date=datetime.date(2025, 1, 6))
    board.add_coverage_check(check)
    assert len(board.coverage_checks) == 1
    
    exported_checks = [c.to_dict() for c in exported.get("coverage", [])]
    assert any(c["role"] == "Nurse" and str(c["date"]) == "2025-01-06" 
               for c in exported_checks), \
        "Coverage check export failed"
    
    print("All import/export tests passed.")

if __name__ == "__main__":
    test_import_export(ShiftBoard())
