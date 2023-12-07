from tkinter import *

from . import album_create
from . import list_album

root = Tk()

root.geometry('500x250')
root.title('Álbuns')

def open():
    build()

    root.mainloop()

def open_album_create(event):
    album_create.open(root)

def open_list_album(event):
    list_album.open(root)

def build():
    pop_album_create = Button(root, text='Adicionar álbum')
    pop_list_album = Button(root, text='Listar álbuns')

    pop_album_create.bind('<Button-1>', open_album_create)
    pop_list_album.bind('<Button-1>', open_list_album)

    pop_album_create.pack()
    pop_list_album.pack()