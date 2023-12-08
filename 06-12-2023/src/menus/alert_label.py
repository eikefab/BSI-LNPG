from tkinter.ttk import Frame, Label

def alert(column: int, row: int, text: str, parent: Frame, columnspan: int = 6):
    label = Label(parent, text=text)
    label.grid(column=column, row=row, pady=(10, 10), columnspan=columnspan)

    def destroy():
        label.destroy()

    label.after(2000, func=destroy)