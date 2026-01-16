import curses
from . import ui
from . import theme

def show_message(stdscr, title, message):
    """Displays a simple message box."""
    height, width = 10, 60
    y, x = (curses.LINES - height) // 2, (curses.COLS - width) // 2
    
    win = ui.Window(height, width, y, x)
    win.draw_border(title)
    
    # Wrap text if needed (simple implementation)
    lines = message.split('\n')
    for idx, line in enumerate(lines):
        if idx < height - 2:
             win.win.addstr(idx + 2, 2, line[:width-4], theme.get_color(theme.COLOR_DEFAULT))
            
    win.win.addstr(height - 2, width // 2 - 4, "[ OK ]", theme.get_color(theme.COLOR_SELECTED))
    
    win.refresh()
    win.getch()

def show_error(stdscr, title, error_msg):
    """Displays an error message box."""
    height, width = 10, 60
    y, x = (curses.LINES - height) // 2, (curses.COLS - width) // 2
    
    win = ui.Window(height, width, y, x)
    # Use Error Color for border
    ui.draw_box(win.win, 0, 0, height, width, title, theme.get_color(theme.COLOR_ERROR))
    
    lines = error_msg.split('\n')
    for idx, line in enumerate(lines):
        if idx < height - 2:
             win.win.addstr(idx + 2, 2, line[:width-4], theme.get_color(theme.COLOR_ERROR))
            
    win.win.addstr(height - 2, width // 2 - 4, "[ OK ]", theme.get_color(theme.COLOR_SELECTED))
    
    win.refresh()
    win.getch()

def ask_input(stdscr, title, prompt):
    """Displays an input box and returns the user input."""
    height, width = 8, 60
    y, x = (curses.LINES - height) // 2, (curses.COLS - width) // 2
    
    win = ui.Window(height, width, y, x)
    win.draw_border(title)
    
    win.win.addstr(2, 2, prompt, theme.get_color(theme.COLOR_DEFAULT))
    
    # Input Area
    input_win = curses.newwin(1, width - 6, y + 4, x + 3)
    input_win.bkgd(' ', theme.get_color(theme.COLOR_INPUT_FIELD))
    
    win.refresh()
    
    curses.echo()
    curses.curs_set(1)
    
    input_win.refresh()
    user_input = input_win.getstr().decode('utf-8')
    
    curses.noecho()
    curses.curs_set(0)
    
    return user_input

def confirm(stdscr, title, question):
    """
    Displays a confirmation dialog. 
    Returns True for Yes, False for No.
    """
    height, width = 10, 60
    y, x = (curses.LINES - height) // 2, (curses.COLS - width) // 2
    
    win = ui.Window(height, width, y, x)
    win.draw_border(title)
    
    win.win.addstr(2, 2, question, theme.get_color(theme.COLOR_DEFAULT))
    
    selected_yes = True
    
    while True:
        # Draw buttons
        btn_y = height - 3
        
        yes_attr = theme.get_color(theme.COLOR_SELECTED) if selected_yes else theme.get_color(theme.COLOR_DEFAULT)
        no_attr = theme.get_color(theme.COLOR_SELECTED) if not selected_yes else theme.get_color(theme.COLOR_DEFAULT)
        
        win.win.addstr(btn_y, width // 2 - 10, " [ YES ] ", yes_attr)
        win.win.addstr(btn_y, width // 2 + 2, " [ NO ] ", no_attr)
        
        win.refresh()
        
        key = win.getch()
        
        if key == curses.KEY_LEFT or key == curses.KEY_RIGHT:
            selected_yes = not selected_yes
        elif key == 10: # Enter
            return selected_yes
        elif key == 27: # Esc
            return False
