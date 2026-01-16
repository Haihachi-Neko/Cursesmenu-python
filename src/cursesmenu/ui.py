import curses
from . import theme

def center_text(text, width):
    """Centers text within a given width."""
    if len(text) >= width:
        return text[:width]
    padding = (width - len(text)) // 2
    return " " * padding + text + " " * (width - len(text) - padding)

def draw_box(win, y, x, height, width, title=None, color=None):
    """
    Draws a box with a specific style.
    """
    if color is None:
        color = theme.get_color(theme.COLOR_BORDER)
    
    win.attron(color)
    # Draw corners
    win.addch(y, x, curses.ACS_ULCORNER)
    win.addch(y, x + width - 1, curses.ACS_URCORNER)
    win.addch(y + height - 1, x, curses.ACS_LLCORNER)
    try:
        win.addch(y + height - 1, x + width - 1, curses.ACS_LRCORNER)
    except curses.error:
        pass
    
    # Draw horizontal lines
    for i in range(1, width - 1):
        win.addch(y, x + i, curses.ACS_HLINE)
        win.addch(y + height - 1, x + i, curses.ACS_HLINE)
        
    # Draw vertical lines
    for i in range(1, height - 1):
        win.addch(y + i, x, curses.ACS_VLINE)
        win.addch(y + i, x + width - 1, curses.ACS_VLINE)
        
    # Draw Title
    if title:
        title_text = f" {title} "
        if len(title_text) < width - 2:
            win.addstr(y, x + 2, title_text, theme.get_color(theme.COLOR_HEADER))
            
    win.attroff(color)

class Window:
    """Wrapper around curses window to simplify usage."""
    def __init__(self, height, width, y, x):
        self.height = height
        self.width = width
        self.win = curses.newwin(height, width, y, x)
        self.win.keypad(True)

    def clear(self):
        self.win.clear()

    def refresh(self):
        self.win.refresh()

    def getch(self):
        return self.win.getch()

    def draw_border(self, title=None):
        draw_box(self.win, 0, 0, self.height, self.width, title)
