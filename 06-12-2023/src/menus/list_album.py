from tkinter import Tk, Toplevel, IntVar
from tkinter.ttk import Frame, Label, Radiobutton, Checkbutton

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
    by = IntVar(value = 0)
    descending = IntVar(value=0)

    columns = ['Álbum', 'Ano de lançamento', 'Autor', 'Álbum de lançamento']
    table_widgets = fill(window)

    def column_order():
        fill(window=window, widgets=table_widgets, data=controller.list_albums_sorted(by.get(), descending=(descending.get() == 1)))

    descending_button = Checkbutton(window, text="Decrescente", variable=descending, command=column_order)
    descending_button.grid(column=4, row=0, pady=(0, 20))

    for table_column in range(len(columns)):
        column = columns[table_column]

        radiobutton = Radiobutton(window, text=column, variable=by, value=table_column, command=column_order)
        radiobutton.grid(column=table_column, row=0, padx=(0, 5), pady=(0, 20))

def fill(window: Toplevel, data: [] = controller.list_albums_sorted(), widgets: [] = []):
    for widget in widgets:
        widget.destroy()

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

            widgets.append(label)
    
    return widgets