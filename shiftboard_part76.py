# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: ShiftBoard
import sys


def handle_keyboard_interrupt():
    try:
        while True:
            try:
                main()
            except KeyboardInterrupt:
                print("\nShiftBoard interrupted. Exiting gracefully.")
                sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
