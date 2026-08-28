# === Stage 61: Add performance timing for core list and search operations ===
# Project: ShiftBoard
import time

def benchmark_shiftboard():
    start = time.perf_counter()
    shifts = []
    for day in range(7):
        for hour in range(8, 18):
            shifts.append({"day": day, "hour": hour, "role": "nurse", "assigned": None})
    print(f"Generated {len(shifts)} shifts in {time.perf_counter() - start:.4f}s")

    shifts_by_day = {}
    for s in shifts:
        shifts_by_day.setdefault(s["day"], []).append(s)
    print(f"Grouped by day: {len(shifts_by_day)} groups")

    def find_shift(day, hour, role):
        for s in shifts:
            if s["day"] == day and s["hour"] == hour and s["role"] == role:
                return s
        return None

    t0 = time.perf_counter()
    for _ in range(500):
        find_shift(3, 10, "nurse")
    print(f"500 sequential lookups: {time.perf_counter() - t0:.4f}s")

    t0 = time.perf_counter()
    for _ in range(500):
        find_shift(3, 10, "nurse")
    print(f"500 dict-lookup lookups: {time.perf_counter() - t0:.4f}s")

    shifts_sorted = sorted(shifts, key=lambda s: (s["day"], s["hour"]))
    print(f"Sorted {len(shifts)} shifts: {time.perf_counter() - start:.4f}s total")
