from tkinter import Tk, Toplevel
from tkinter.ttk import Frame, Label

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import controller

def open(root: Tk):
    window = Toplevel(root)

    frame = Frame(window, padding=30)
    frame.grid()

    window.title("Álbuns")
    window.geometry('600x600')

    build(window, frame)

def build(parent: Toplevel, window: Frame):
    data = controller.list_albums()

    columns = ['Álbum', 'Ano de lançamento', 'Autor', 'Álbum de lançamento']

    for table_column in range(len(columns)):
        column = columns[table_column]

        label = Label(window, text=column)
        label.grid(column=table_column, row=0, padx=(0, 5), pady=(0, 20))

    for row in range(len(data)):
        info = data[row]
        
        for column in range(len(info)):
            column_data = info[column]

            if column_data == 'True':
                column_data = 'Sim'
            elif column_data == 'False':
                column_data = 'Não'

            label = Label(window, text=column_data)
            label.grid(column=column, row=(row + 1), padx=(0, 5), pady=(0, 5))

    