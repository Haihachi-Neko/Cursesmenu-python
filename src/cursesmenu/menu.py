import curses
from . import ui
from . import theme

class SelectionMenu:
    def __init__(self, items, title="Menu"):
        self.items = items
        self.title = title
        self.selection = 0
        
    def show(self, stdscr):
        """Displays the menu and returns the selected index or -1 if cancelled."""
        height = len(self.items) + 6
        width = 50
        y, x = (curses.LINES - height) // 2, (curses.COLS - width) // 2
        
        win = ui.Window(height, width, y, x)
        
        while True:
            win.clear()
            win.draw_border(self.title)
            
            for idx, item in enumerate(self.items):
                item_y = 3 + idx
                if idx == self.selection:
                    attr = theme.get_color(theme.COLOR_SELECTED)
                    text = f"> {item} <" 
                else:
                    attr = theme.get_color(theme.COLOR_DEFAULT)
                    text = f"  {item}  "
                
                centered = ui.center_text(text, width - 2)
                win.win.addstr(item_y, 1, centered, attr)
                
            win.refresh()
            
            key = win.getch()
            
            if key == curses.KEY_UP:
                self.selection = (self.selection - 1) % len(self.items)
            elif key == curses.KEY_DOWN:
                self.selection = (self.selection + 1) % len(self.items)
            elif key == 10: # Enter
                return self.selection
            elif key == ord('q') or key == 27: # q or Esc
                return -1
