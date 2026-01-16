import curses
import time
from . import ui
from . import theme

class ProgressBar:
    def __init__(self, title="Progress", total=100):
        self.title = title
        self.total = total
        self.current = 0
        
    def show(self, stdscr, progress_func=None):
        """
        Displays the progress bar.
        If progress_func is provided, it calls it to update progress.
        Otherwise, it just shows the bar and lets the caller update.
        """
        height, width = 8, 60
        y, x = (curses.LINES - height) // 2, (curses.COLS - width) // 2
        
        win = ui.Window(height, width, y, x)
        
        # Initial draw
        self.update(win, 0)
        
        if progress_func:
            for i in range(self.total + 1):
                self.update(win, i)
                progress_func(i)
                time.sleep(0.05) # Simulation delay
                
        win.getch() # Wait for key press after done
        
    def update(self, win, value):
        self.current = value
        
        win.clear()
        win.draw_border(self.title)
        
        # Calculate bar width
        bar_width = win.width - 4
        filled_len = int(bar_width * (self.current / self.total))
        
        bar_str = "[" + "|" * filled_len + " " * (bar_width - filled_len) + "]"
        
        # Draw Bar
        # We need to draw part of it green and part of it empty (maybe based on chars)
        # For simplicity, we just print the string, but we can color the pipes.
        
        win.win.addstr(win.height // 2 - 1, 2, "[", theme.get_color(theme.COLOR_DEFAULT))
        
        for i in range(bar_width):
            char = "|" if i < filled_len else " "
            color = theme.get_color(theme.COLOR_PROGRESS_FULL) if i < filled_len else theme.get_color(theme.COLOR_PROGRESS_EMPTY)
            win.win.addch(win.height // 2 - 1, 3 + i, char, color)
            
        win.win.addstr(win.height // 2 - 1, 2 + bar_width + 1, "]", theme.get_color(theme.COLOR_DEFAULT))
        
        # Percentage
        percent = int((self.current / self.total) * 100)
        percent_str = f"{percent}%"
        win.win.addstr(win.height // 2 + 1, win.width // 2 - len(percent_str) // 2, percent_str, theme.get_color(theme.COLOR_HEADER))
        
        win.refresh()
