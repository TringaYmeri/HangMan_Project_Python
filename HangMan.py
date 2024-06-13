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




    def guess_letter(event=None):

        nonlocal lives
        letter = letter_entry.get().lower()

        if not letter:
            messagebox.showerror("Gabim", "Ju lutem shtypni nje shkronje!")
            return

        if len(letter) != 1 or not letter.isalpha():
            messagebox.showerror(
                "Gabim", "Ju lutem shkruani vetem nje shkronje!")
            letter_entry.delete(0, 'end')
            return

        elif not letter.isalpha():
            messagebox.showerror(
                "Gabim", "Ju lutem shkruani vetem shkronja!")
            letter_entry.delete(0, 'end')
            return

        if letter.isalpha() and len(letter) == 1:
            if letter in guessed_letters:
                messagebox.showinfo(
                    "Gabim", "Keni marre kete shkronje tashme!")

            elif letter in word:
                guessed_letters.append(letter)
                for i, char in enumerate(word):
                    if char == letter:
                        display_word[i] = letter
                word_label.config(text=' '.join(display_word))
                if '_' not in display_word:
                    messagebox.showinfo("Fitore", "Urime! Ju fituat!")
                    play_again()
            else:
                messagebox.showinfo(
                    "Gabim", "Shkronja '{}' nuk eshte ne fjale!".format(letter))
                guessed_letters.append(letter)
                lives -= 1
                lives_label.config(text="Tentativa: {}".format(lives))
                if lives == 0:
                    messagebox.showinfo(
                        "Deshperim", f"Ju humbet!. Fjala ishte '{word}'!")
                    play_again()
            letter_entry.delete(0, 'end')

    def play_again():
        response = messagebox.askyesno(
            "Loje perfundoi", "Deshironi te luani perseri?")
        if response:
            root.destroy()
            initialize_gui()
        else:
            root.quit()
            sys.exit(0)


    word_label = tk.Label(root, text=' '.join(
        display_word), font=("Helvetica", 16))
    word_label.pack()

    letter_label = tk.Label(
        root, text="Shtypni nje shkronje:", font=("Helvetica", 12))
    letter_label.pack(pady=5)

    letter_entry = tk.Entry(root, font=("Helvetica", 12))
    letter_entry.pack()

    guess_button = tk.Button(
        root, text="Supozo", command=guess_letter, font=("Helvetica", 12))
    guess_button.pack(pady=5)

    root.bind('<Return>', guess_letter)

    lives_label = tk.Label(root, text="Tentativa: {}".format(
        lives), font=("Helvetica", 12))
    lives_label.pack()


def show_about():
    about_message = "Keni mundesine prej 3 nivele per te zgjedhur.\n"
    about_message += "Jane 5 kategori te fjaleve qe mundeni te zgjedhni.\n"
    about_message += "\n-Niveli 'easy' jep 8 tentativa, dhe ka zgjedhje kategorie.\n"
    about_message += "\n-Niveli 'moderate' jep 6 tentativa, dhe ka zgjedhje kategorie.\n"
    about_message += "\n-Niveli 'hard' jep 4 tentativa, dhe nuk ka zgjedhje kategorie.\n"
    messagebox.showinfo("Rreth Lojes Hangman", about_message)

if __name__ == "__main__":
    initialize_gui()
