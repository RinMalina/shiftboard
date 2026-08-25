# === Stage 55: Add a setting to disable colorized output ===
# Project: ShiftBoard
import sys
from io import StringIO

class ColorSettings:
    """Configuration for controlling color output in the terminal."""

    def __init__(self):
        self._enabled = sys.stdout.isatty()
        self._disabled = False
        self._original_stdout = None
        self._original_stderr = None
        self._redirected = False
        self._original_color = None

    @property
    def enabled(self):
        """Return whether color output is currently enabled."""
        return not self._disabled

    def disable(self):
        """Disable color output by redirecting stdout/stderr to StringIO buffers."""
        self._disabled = True
        if not self._redirected:
            self._original_stdout = sys.stdout
            self._original_stderr = sys.stderr
            sys.stdout = StringIO()
            sys.stderr = StringIO()
            self._redirected = True
            self._original_color = sys.stdout.isatty()

    def enable(self):
        """Re-enable color output by restoring original stdout/stderr."""
        self._disabled = False
        if self._redirected:
            sys.stdout = self._original_stdout
            sys.stderr = self._original_stderr
            self._redirected = False
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

    def reset(self):
        """Reset the color setting to its default state."""
        self._disabled = False
        self._redirected = False
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        self._original_color = sys.stdout.isatty()

    def is_color_enabled(self):
        """Check if color output is currently enabled."""
        return not self._disabled
