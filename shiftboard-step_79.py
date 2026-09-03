# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: ShiftBoard
def main():
    from shiftboard import ShiftBoard
    board = ShiftBoard()
    board.add_role("Nurse", "nurse")
    board.add_role("Assistant", "assistant")
    board.add_availability("mon", ["nurse", "assistant"])
    board.add_availability("tue", ["nurse", "assistant"])
    board.add_availability("wed", ["nurse", "assistant"])
    board.add_availability("thu", ["nurse", "assistant"])
    board.add_availability("fri", ["nurse", "assistant"])
    board.add_availability("sat", ["nurse", "assistant"])
    board.add_availability("sun", ["nurse", "assistant"])
    board.add_shift("mon", ["nurse", "assistant"])
    board.add_shift("tue", ["nurse", "assistant"])
    board.add_shift("wed", ["nurse", "assistant"])
    board.add_shift("thu", ["nurse", "assistant"])
    board.add_shift("fri", ["nurse", "assistant"])
    board.add_shift("sat", ["nurse", "assistant"])
    board.add_shift("sun", ["nurse", "assistant"])
    board.validate()
    board.print_roster()

    print("ShiftBoard demo complete!")

if __name__ == "__main__":
    main()
