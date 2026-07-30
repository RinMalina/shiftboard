# === Stage 38: Add data integrity checks for broken references ===
# Project: ShiftBoard
def check_integrity(db_path, logger=None):
    if logger is None:
        import logging
        logger = logging.getLogger("shiftboard.integrity")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check for orphaned shifts (no employee_id or role_id that exist)
        cursor.execute("""
            SELECT COUNT(*) FROM shifts s
            LEFT JOIN employees e ON s.employee_id = e.id
            WHERE e.id IS NULL
        """)
        orphan_shifts = cursor.fetchone()[0]
        
        if orphan_shifts > 0:
            logger.warning(f"{orphan_shifts} shift(s) reference non-existent employee(s)")
            
        # Check for swaps referencing unavailable employees
        cursor.execute("""
            SELECT COUNT(*) FROM shifts s1
            JOIN shifts s2 ON s1.swap_id = s2.id
            WHERE s2.employee_id NOT IN (SELECT id FROM employees WHERE active = 1)
        """)
        bad_swaps = cursor.fetchone()[0]
        
        if bad_swaps > 0:
            logger.warning(f"{bad_swaps} swap(s) reference inactive employee(s)")
            
    except sqlite3.Error as e:
        logger.error(f"Integrity check failed: {e}")
