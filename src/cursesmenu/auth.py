import curses
import subprocess
import sys
import random
import os
import string
from . import dialogs
from . import ui
from . import theme

def generate_code(length=6):
    """Generates a random alphanumeric code."""
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def perform_gui_auth(stdscr):
    """
    Launches a GUI window which displays a code and asks for input.
    Returns True if successful, False otherwise.
    """
    code = generate_code()
    
    # Path to the gui script.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    gui_script = os.path.join(current_dir, 'gui_input.py')
    
    # Show waiting message in TUI
    height, width = 8, 50
    y, x = (curses.LINES - height) // 2, (curses.COLS - width) // 2
    win = ui.Window(height, width, y, x)
    win.draw_border("Authentication In Progress")
    
    msg = "Follow instructions in the"
    msg2 = "external secure window."
    win.win.addstr(3, width // 2 - len(msg) // 2, msg, theme.get_color(theme.COLOR_DEFAULT))
    win.win.addstr(4, width // 2 - len(msg2) // 2, msg2, theme.get_color(theme.COLOR_DEFAULT))
    win.win.addstr(6, width // 2 - 10, "Waiting for input...", theme.get_color(theme.COLOR_DEFAULT) | curses.A_BLINK)
    win.refresh()
    
    # Launch GUI in a subprocess and capture output
    try:
        # Pass the code as an argument to the GUI script
        result = subprocess.run([sys.executable, gui_script, code], capture_output=True, text=True)
        user_input = result.stdout.strip()
    except Exception as e:
        dialogs.show_error(stdscr, "System Error", f"Failed to launch GUI:\n{str(e)}")
        return False

    # Check result
    if user_input.upper() == code:
        dialogs.show_message(stdscr, "Success", "Authentication Verified.")
        return True
    else:
        dialogs.show_error(stdscr, "Access Denied", f"Incorrect Code.\nExpected: {code}\nReceived: {user_input}")
        return False
