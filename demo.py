import curses
import sys
import os

# Ensure we can import the package
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from cursesmenu import theme, ui, dialogs, menu, progress, auth

def main(stdscr):
    # Initialize Theme
    try:
        theme.init_theme()
    except Exception as e:
        # Fallback if colors fail
        pass

    # Main Menu Items
    items = [
        "Show Message",
        "Ask Input",
        "Confirm Action",
        "Show Error",
        "Progress Bar Demo",
        "GUI Authentication",
        "Exit"
    ]
    
    main_menu = menu.SelectionMenu(items, title="CYBER MENU SYSTEM v1.0")
    
    while True:
        selection = main_menu.show(stdscr)
        
        if selection == 0: # Message
            dialogs.show_message(stdscr, "System Info", "This is demo message")
            
        elif selection == 1: # Input
            name = dialogs.ask_input(stdscr, "Identification", "Enter your name:")
            if name:
                dialogs.show_message(stdscr, "Welcome", f"Hello, {name}.")
                
        elif selection == 2: # Confirm
            if dialogs.confirm(stdscr, "Confirm", "Confirm demo"):
                dialogs.show_message(stdscr, "Info", "YES")
            else:
                dialogs.show_message(stdscr, "Info", "NO")
                
        elif selection == 3: # Error
            dialogs.show_error(stdscr, "ERROR", "ERROR")
            
        elif selection == 4: # Progress
            p = progress.ProgressBar("Processing", total=100)
            def dummy_work(i):
                pass
            p.show(stdscr, progress_func=dummy_work)
            
        elif selection == 5: # GUI Auth
            auth.perform_gui_auth(stdscr)

        elif selection == 6 or selection == -1: # Exit
            break

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except ImportError:
        print("Error: windows-curses or curses is not installed.")
        print("Please run: pip install windows-curses")
