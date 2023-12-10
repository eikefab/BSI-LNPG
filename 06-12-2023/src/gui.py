from tkinter import Tk, Menu
from tkinter.ttk import Frame
from utils import Album, AlbumTable
from controller import add, get

def open():
    window = Tk()

    menu = Menu(window, tearoff=0)
    menu.add_command(label="Adicionar álbum", command=window.destroy)
    menu.add_separator()

    widgets = Frame(window)
    widgets.pack()

    window.resizable(0, 0)
    window.title("Álbuns")
    window.geometry("600x600")

    table = AlbumTable(get())
    table_content = table.build(widgets)

    table.update(get(order=lambda album: album.year))

    window.config(menu=menu)
    window.mainloop()
    


