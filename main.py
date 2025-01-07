import tkinter as tk
from tkinter import messagebox
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def show_height():
    try:
        height = int(entry.get())
        messagebox.showinfo("Result", f"Your height is {height} cm!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.iconbitmap(default=resource_path('trans.ico'))
root.title("Height Calculator Tool")

label = tk.Label(root, text="Input your height")
label.pack(pady=5)
root.geometry("300x150")

label = tk.Label(root, text="Input your height")
label.place(x=10, y=40)

entry = tk.Entry(root, width=10)
entry.place(x=150, y=40)

button = tk.Button(root, text="Calculate", command=show_height)
button.place(x=210, y=100)

root.mainloop()
