# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ShiftBoard
def print_shift_table(shifts):
    if not shifts:
        print("No shifts scheduled.")
        return
    headers = ["ID", "Staff", "Role", "Date", "Time"]
    widths = [6, 12, 8, 14, 10]
    for i in range(5):
        line = "".join(str(shifts[j][i]).ljust(widths[i]) if i < len(shifts[0]) else "" for j in range(len(shifts)))
        print(line)
    return
