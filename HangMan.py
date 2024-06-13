import tkinter as tk
from tkinter import messagebox
import pyodbc
import random
import sys
import os
import logging
logging.basicConfig(level=logging.DEBUG)


def quit_application():
    try:
        root.destroy()
        sys.exit(0)
    except Exception as e:
        print("Ka ndodhur nje gabim gjate daljes nga programi:", e)


def initialize_gui():
    global root, welcome_label, name_label, name_entry, show_button
    root = tk.Tk()
    root.title("Miresevini ne Lojen HangMan")
    root.geometry("600x300")

    welcome_label = tk.Label(
        root, text="Miresevini ne Lojen HangMan", font=("Helvetica", 24))
    welcome_label.pack(pady=20)

    name_label = tk.Label(
        root, text="Ju lutem shkruani emrin tuaj:", font=("Helvetica", 14))
    name_label.pack()

    name_entry = tk.Entry(root, font=("Helvetica", 12))
    name_entry.pack()
    name_entry.focus()

    show_button = tk.Button(root, text="Jam Gati",
                            command=show_options, font=("Helvetica", 12))
    show_button.pack(pady=10)

    name_entry.bind('<Return>', show_options)
    root.mainloop()

def show_options(event=None):
    global name_entry
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Kujdes", "Ju lutem shkruani emrin tuaj!")
        return
    elif not name.isalpha():
        messagebox.showerror("Kujdes", "Emri duhet te permbaje vetem shkronja")
        name_entry.delete(0, 'end')
        return

    response = messagebox.askyesno(f"Tungjatjeta", f"{name}! A jeni Gati?")
    if response:
        global show_button, play_button, about_button, quit_button, title_label
        welcome_label.destroy()
        name_label.destroy()
        name_entry.destroy()
        show_button.destroy()

        title_label = tk.Label(
            root, text="Zgjidhni njerin nga opsionet e meposhtme", font=("Helvetica", 14))
        title_label.pack(pady=10)

        play_button = tk.Button(
            root, text="Luaj Lojen", command=show_levels, font=("Helvetica", 12), width=20)
        play_button.pack(pady=5)


        about_button = tk.Button(
            root, text="Rreth Lojes", command=show_about, font=("Helvetica", 12), width=20)
        about_button.pack(pady=5)

        quit_button = tk.Button(
            root, text="Dil", command=quit_application, font=("Helvetica", 12), width=20)
        quit_button.pack(pady=5)
    else:
        messagebox.showinfo("Na vjen keq", "Luaj lojen kur te jeni gati!")
        root.destroy()
