
import tkinter as tk
from tkinter import ttk, messagebox

def choose_option(options):
    root = tk.Tk()  # creates the window 
    root.title("Choose an option")

    token = tk.StringVar()  # variable to save the choice

    def confirm():
        option = combo.get()
        if option:
            token.set(option)
            root.destroy()
        else:
            messagebox.showwarning("Attention", "Choose an option before clicking confirm!")

    # UI
    tk.Label(root, text="Choose from the following:", font=("Arial", 12)).pack(pady=10)

    combo = ttk.Combobox(root, values=options, state="readonly")
    combo.pack(pady=5)

    tk.Button(root, text="Confirm", command=confirm).pack(pady=10)

    root.mainloop()  # keeps the window open until root.destroy()

    return token.get()  # return the final value
