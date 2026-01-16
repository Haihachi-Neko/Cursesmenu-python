import curses

# Color pair IDs
COLOR_DEFAULT = 1
COLOR_HEADER = 2
COLOR_SELECTED = 3
COLOR_BORDER = 4
COLOR_ERROR = 5
COLOR_PROGRESS_EMPTY = 6
COLOR_PROGRESS_FULL = 7
COLOR_INPUT_FIELD = 8

def init_theme():
    """
    Initializes the Cyber theme colors.
    Must be called after curses.initscr() and curses.start_color().
    """
    if not curses.has_colors():
        return

    curses.use_default_colors()

    # Text, Background
    curses.init_pair(COLOR_DEFAULT, curses.COLOR_GREEN, curses.COLOR_BLACK)       # Default text: Neon Green on Black
    curses.init_pair(COLOR_HEADER, curses.COLOR_CYAN, curses.COLOR_BLACK)         # Headers: Cyan on Black
    curses.init_pair(COLOR_SELECTED, curses.COLOR_BLACK, curses.COLOR_GREEN)      # Selected: Black on Green
    curses.init_pair(COLOR_BORDER, curses.COLOR_MAGENTA, curses.COLOR_BLACK)      # Borders: Magenta on Black
    curses.init_pair(COLOR_ERROR, curses.COLOR_RED, curses.COLOR_BLACK)           # Error: Red on Black
    
    # Progress Bar
    curses.init_pair(COLOR_PROGRESS_EMPTY, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(COLOR_PROGRESS_FULL, curses.COLOR_BLACK, curses.COLOR_GREEN)
    
    # Input
    curses.init_pair(COLOR_INPUT_FIELD, curses.COLOR_CYAN, curses.COLOR_BLACK)

def get_color(color_id):
    return curses.color_pair(color_id)
