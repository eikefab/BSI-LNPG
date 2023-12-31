from tkinter import Tk, Toplevel, IntVar, StringVar
from tkinter.ttk import Frame, Entry, Label, Button, Checkbutton
from .alert_label import alert

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import controller


def open(root: Tk):
    window = Toplevel(root)
    window.resizable(False, False)

    frame = Frame(window, padding=30)
    frame.grid()

    window.title("Adicionar álbum")
    window.geometry("400x250")

    build(window, frame)


def build(parent: Toplevel, window: Frame):
    debut = IntVar(value=0)
    album = StringVar()
    release_year = StringVar()
    author = StringVar()

    album_input = Entry(window, textvariable=album)
    release_year_input = Entry(window, textvariable=release_year)
    author_input = Entry(window, textvariable=author)

    album_input_label = Label(window, text="Nome:")
    release_year_input_label = Label(window, text="Ano:")
    author_input_label = Label(window, text="Autor (Banda/Artista):")

    debut_input = Checkbutton(window, text="Álbum de lançamento", variable=debut)

    register_button = Button(window, text="Registrar")

    album_input_label.grid(column=0, row=1, padx=(0, 5), pady=(10, 0), sticky="W")
    release_year_input_label.grid(
        column=0, row=2, padx=(0, 5), pady=(10, 0), sticky="W"
    )
    author_input_label.grid(column=0, row=3, padx=(0, 5), pady=(10, 0), sticky="W")

    album_input.grid(column=1, row=1, pady=(10, 0))
    release_year_input.grid(column=1, row=2, pady=(10, 0))
    author_input.grid(column=1, row=3, pady=(10, 0))
    debut_input.grid(column=1, row=4, pady=(10, 0))

    register_button.grid(column=1, row=5, pady=(10, 0))

    def handle_alert(text):
        alert(0, 0, text, window)

    def add_album(event):
        created = controller.create_album(
            album.get(),
            release_year.get(),
            author.get(),
            (debut.get() == 1),
            handle_alert,
        )

        if created:
            album.set("")
            release_year.set("")
            author.set("")
            debut.set(0)

    register_button.bind("<Button-1>", add_album)
    register_button.bind("<Return>", add_album)
