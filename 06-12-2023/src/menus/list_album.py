from tkinter import Tk, Toplevel, IntVar, StringVar
from tkinter.ttk import Frame, Label, Radiobutton, Checkbutton, Entry, Button
from .alert_label import alert

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import controller

data = controller.list_albums()


def open(root: Tk):
    window = Toplevel(root)
    window.resizable(False, False)

    frame = Frame(window, padding=30)
    frame.grid()

    window.title("Álbuns")
    window.geometry("850x600")

    build(window, frame)


def build(parent: Toplevel, window: Frame):
    global data

    by = IntVar(value=0)
    descending = IntVar(value=0)
    filter_data = StringVar()
    filter_type = IntVar(value=0)
    filter_year_type = IntVar(value=0)

    columns = ["Álbum", "Ano de lançamento", "Autor", "Álbum de lançamento"]

    table_widgets = fill(window)
    year_search_widgets = []

    def column_order():
        global data

        fill(
            window=window,
            widgets=table_widgets,
            data=controller.sort_albums(
                data, by.get(), descending=(descending.get() == 1)
            ),
        )

    def clear_filter():
        global data

        data = controller.list_albums()

        column_order()

    def hide_year_search():
        for widget in year_search_widgets:
            widget.destroy()

    def show_year_search():
        equal = Radiobutton(window, text="Igual a", variable=filter_year_type, value=0)
        greater = Radiobutton(
            window, text="Maior que", variable=filter_year_type, value=1
        )
        lower = Radiobutton(
            window, text="Menor que", variable=filter_year_type, value=2
        )

        equal.grid(column=0, row=3, pady=(5, 0), sticky="W")
        greater.grid(column=0, row=4, pady=(5, 0), sticky="W")
        lower.grid(column=0, row=5, pady=(5, 0), sticky="W")

        year_search_widgets.append(equal)
        year_search_widgets.append(greater)
        year_search_widgets.append(lower)

    def filter_results():
        global data

        content = filter_data.get()
        type = filter_type.get()

        if type == 0:
            if len(content) == 0:
                alert(0, 0, "Nome precisa ser válido!", window, 1)

                return

            data = controller.get_albums_by_author(content)
        else:
            year_type = filter_year_type.get()

            if not content.isdigit():
                alert(0, 0, "Ano precisa ser válido!", window, 1)

                return

            year = int(content)

            if year_type == 0:
                data = controller.get_albums_by_year(year)
            else:
                data = controller.filter_albums_by_year(year, (year_type == 1))

        fill(
            window=window,
            data=controller.sort_albums(
                data, by.get(), descending=(descending.get() == 1)
            ),
        )

    descending_button = Checkbutton(
        window, text="Inverter ordem", variable=descending, command=column_order
    )
    descending_button.grid(column=0, row=9, pady=(10, 0), sticky="W")

    filter = Entry(window, textvariable=filter_data)
    filter_label = Label(window, text="Procurar por:")

    filter_author = Radiobutton(
        window, text="Autor", variable=filter_type, value=0, command=hide_year_search
    )
    filter_year = Radiobutton(
        window, text="Ano", variable=filter_type, value=1, command=show_year_search
    )

    filter_action = Button(window, text="Filtrar", command=filter_results)
    filter_clear_action = Button(window, text="Limpar filtro", command=clear_filter)

    filter_label.grid(column=0, row=1, padx=(0, 5), pady=(0, 20), sticky="W")
    filter_author.grid(column=0, row=2, pady=(5, 0), sticky="W")
    filter_year.grid(column=0, row=3, pady=(5, 0), sticky="W")
    filter_action.grid(column=0, row=7, pady=(15, 5), sticky="W")
    filter_clear_action.grid(column=0, row=8, pady=(5, 5), sticky="W")

    filter.grid(column=1, row=1, pady=(0, 20), padx=(0, 20))

    for table_column in range(len(columns)):
        column = columns[table_column]

        radiobutton = Radiobutton(
            window, text=column, variable=by, value=table_column, command=column_order
        )
        radiobutton.grid(column=(table_column + 2), row=0, pady=(0, 20), padx=(20, 0))


def fill(
    window: Toplevel, data: [] = controller.list_albums_sorted(), widgets: [] = []
):
    for widget in widgets:
        widget.destroy()

    if len(data) == 0:
        label = Label(
            window, text="Nenhum resultado encontrado para o filtro informado."
        )
        label.grid(column=2, row=1, pady=(5, 0), columnspan=10)

        widgets.append(label)

        return

    for row in range(len(data)):
        info = data[row]

        for column in range(len(info)):
            column_data = info[column]

            if column_data == "True":
                column_data = "Sim"
            elif column_data == "False":
                column_data = "Não"

            label = Label(window, text=column_data)
            label.grid(column=(column + 2), row=(row + 1), pady=(5, 0), padx=(20, 0))

            widgets.append(label)

    return widgets
