# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ShiftBoard
class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    def __init__(self, code):
        self.code = code

    def __call__(self, text):
        if os.environ.get("NO_COLOR"):
            return text
        return self.code + text + self.RESET

    def __str__(self):
        return self.code

    def __repr__(self):
        return f"Color({self.code!r})"
