import tkinter as tk
import sys

def main():
    if len(sys.argv) < 2:
        # Fallback or error if no code passed
        target_code = "UNKNOWN"
    else:
        target_code = sys.argv[1]

    root = tk.Tk()
    root.title("SECURE AUTHENTICATION")
    root.geometry("400x300")
    root.configure(bg='black')

    # Frame
    frame = tk.Frame(root, bg='black', highlightbackground='#00aa00', highlightthickness=2)
    frame.pack(expand=True, fill='both', padx=10, pady=10)

    # Instruction Label
    label_instr = tk.Label(frame, text="TYPE THE CODE BELOW:", font=("Consolas", 12), fg='#00aaaa', bg='black')
    label_instr.pack(pady=(20, 5))

    # Code Display Label
    label_code = tk.Label(frame, text=target_code, font=("Consolas", 24, "bold"), fg='#ff00ff', bg='black')
    label_code.pack(pady=(5, 20))

    # Entry
    entry_code = tk.Entry(frame, font=("Consolas", 18), fg='#00ff00', bg='#222222', insertbackground='#00ff00', justify='center')
    entry_code.pack(pady=10, padx=50)
    entry_code.focus_set()

    def submit(event=None):
        code = entry_code.get()
        print(code) # Print to stdout for confirmation
        root.destroy()

    # Bind Enter key
    root.bind('<Return>', submit)

    # Submit Button
    btn_submit = tk.Button(frame, text="[ AUTHENTICATE ]", command=submit, 
                          font=("Consolas", 12), fg='black', bg='#00aaaa', 
                          activebackground='#00ff00', activeforeground='black', relief='flat')
    btn_submit.pack(pady=(10, 20))

    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    root.geometry('{}x{}+100+100'.format(width, height,))

    root.mainloop()

if __name__ == "__main__":
    main()
