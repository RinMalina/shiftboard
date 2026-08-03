# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ShiftBoard
import unittest
from shiftboard.models import Shift, StaffMember, Role, ScheduleEntry
from datetime import date


def make_entry(week=0):
    return ScheduleEntry(
        week=week, day="Mon", hour=9, minute=0, role=Role.NURSE, member_id="m1"
    )


class TestUpdateDeleteEdgeCases(unittest.TestCase):

    def test_update_to_zero_hours(self):
        entry = make_entry()
        new = ScheduleEntry(week=entry.week, day="Mon", hour=5, minute=0, role=Role.NURSE, member_id="m1")
        updated = entry.update(new)
        self.assertEqual(updated.hours_worked, 5)
        self.assertEqual(updated.total_hours, 32.0 - 9 + 5)

    def test_update_preserves_week(self):
        e1 = make_entry(week=3)
        new = ScheduleEntry(week=3, day="Tue", hour=10, minute=0, role=Role.NURSE, member_id="m2")
        updated = e1.update(new)
        self.assertEqual(updated.week, 3)

    def test_update_changes_member(self):
        e = make_entry()
        new = ScheduleEntry(week=e.week, day="Mon", hour=9, minute=0, role=Role.NURSE, member_id="m2")
        updated = e.update(new)
        self.assertEqual(updated.member_id, "m2")

    def test_delete_removes_entry(self):
        entry = make_entry()
        schedule = ScheduleEntry(week=entry.week, day="Mon", hour=9, minute=0, role=Role.NURSE, member_id="m1")
        self.assertEqual(len(entry.schedule), 1)
        del entry.schedule[0]
        self.assertEqual(len(entry.schedule), 0)

    def test_delete_nonexistent_raises(self):
        entry = make_entry()
        schedule = ScheduleEntry(week=entry.week, day="Mon", hour=9, minute=0, role=Role.NURSE, member_id="m1")
        with self.assertRaises(IndexError):
            del entry.schedule[5]

    def test_update_empty_schedule(self):
        e = ScheduleEntry(week=0, day="", hour=0, minute=0, role=None, member_id="")
        new = make_entry()
        updated = e.update(new)
        self.assertEqual(len(updated.schedule), 1)


if __name__ == "__main__":
    unittest.main()
