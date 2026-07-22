# === Stage 16: Add argparse support for the most common commands ===
# Project: ShiftBoard
import argparse
from shiftboard import ShiftBoard, Role, Availability, Swap, WeeklyRoster

def main():
    parser = argparse.ArgumentParser(description="ShiftBoard - Staff shift scheduler")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # add-role command
    role_parser = subparsers.add_parser('add-role')
    role_parser.add_argument('--name', type=str, help='Role name (e.g. Nurse, Driver)')

    # add-availability command
    avail_parser = subparsers.add_parser('add-availability')
    avail_parser.add_argument('--role', type=str, help='Role name')
    avail_parser.add_argument('--dates', nargs='+', type=str, help='Available dates (YYYY-MM-DD)')

    # add-swap command
    swap_parser = subparsers.add_parser('add-swap')
    swap_parser.add_argument('--from-employee', type=str, required=True)
    swap_parser.add_argument('--to-employee', type=str, required=True)
    swap_parser.add_argument('--date', type=str, help='Date of the swap (YYYY-MM-DD)')

    # generate-roster command
    roster_parser = subparsers.add_parser('generate-roster')
    roster_parser.add_argument('--week-start', type=int, default=0, help='Day offset from Monday (0-6)')

    args = parser.parse_args()

    if args.command == 'add-role':
        board = ShiftBoard()
        role = Role(args.name)
        board.add_role(role)
        print(f"Role '{args.name}' added.")

    elif args.command == 'add-availability':
        board = ShiftBoard()
        role = Role(args.role)
        board.add_role(role)
        for date in args.dates:
            availability = Availability(date, role)
            board.add_availability(availability)
        print(f"Availability added for {len(args.dates)} dates under '{args.role}'.")

    elif args.command == 'add-swap':
        board = ShiftBoard()
        swap = Swap(args.from_employee, args.to_employee, date=args.date)
        board.add_swap(swap)
        print("Swap recorded successfully.")

    elif args.command == 'generate-roster':
        board = ShiftBoard()
        roster = WeeklyRoster(board.roles, start_day=args.week_start)
        board.assign_roster(roster)
        print("Weekly roster generated. Check the board for assignments and conflicts.")

if __name__ == '__main__':
    main()
