from tkinter.ttk import Frame, Label, Widget


class Album:
    def __init__(self, name: str, year: int, author: str, debut: int | bool):
        self.name = name
        self.year = year
        self.author = author
        self.debut = debut

    def to_list(self) -> list[str]:
        """
        Returns the album's data as list
        """

        return [self.name, str(self.year), self.author, self.debut]


class AlbumTable:
    def __init__(
        self, data: list[Album] = [], order_index: int = 0, widgets: list[Widget] = []
    ):
        self.data = data
        self.order_index = order_index
        self.widgets = widgets

    def columns(self) -> list[str]:
        return ["Nome", "Ano", "Autor/Banda", "Estréia"]

    def update(self, data: list[Album], order_index: int = 0) -> None:
        """
        Updates the table within the given data
        """

        self.order_index = order_index
        self.data = self.order(data, order_index)

        for widget in self.widgets:
            widget.destroy()

        self.build(self.parent, self.position)

    def order(self, data: list[Album], index: int = 0):
        return sorted(data, key=lambda album: album.to_list()[index])

    def build(self, parent: Frame, position: tuple[int, int] = (0, 0)) -> list[Widget]:
        """
        Build the table at the frame and returns all widgets used on it
        """

        self.parent = parent
        self.position = position

        frame = Frame(parent, padding=30)
        frame.grid(column=0, row=1)

        widgets = self.widgets
        start_column, start_row = position

        columns = self.columns()
        data = self.data

        for column in range(len(columns)):
            column_title = columns[column]

            column_label = Label(frame, text=column_title, font=("Arial", 12, "bold"))
            column_label.grid(
                column=(start_column + column),
                row=start_row,
                padx=20,
                pady=10,
                sticky="W",
            )

            widgets.append(column_label)

        if len(data) == 0:
            label = Label(frame, text="Nenhum álbum encontrado.", font=("Arial", 12))
            label.grid(columnspan=4, column=start_column, row=(start_row + 1))

            widgets.append(label)

        for data_row in range(len(data)):
            album: Album = data[data_row]

            for data_column in range(len(columns)):
                album_column_data = album.to_list()[data_column]

                if data_column == 3:
                    album_column_data = "Sim" if album_column_data == "True" else "Não"

                data_column_label = Label(
                    frame, text=album_column_data, font=("Arial", 12)
                )
                data_column_label.grid(
                    column=(start_column + data_column),
                    row=((start_row + 1) + data_row),
                    padx=20,
                    sticky="W",
                )

                widgets.append(data_column_label)

        return widgets
