from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

times = 0
data = ("Azul", "Verde", "Vermelho")
radio_value = IntVar(value=0)
checkbox_value_a = IntVar(value=0)
checkbox_value_b = IntVar(value=0)

window.title("Olá Mundo!")
window.geometry("500x250")

label = Label(window, text="Olá!")
textbox = Entry(window, text="Teste!", bd=3)
combobox = Combobox(window, values=data)
listbox = Listbox(window, height=5, selectmode='multiple')

radio_a = Radiobutton(window, text="Programação", variable=radio_value, value=0)
radio_b = Radiobutton(window, text="Infra", variable=radio_value, value=1)

checkbox_a = Checkbutton(window, text="Futebol", variable=checkbox_value_a)
checkbox_b = Checkbutton(window, text="Tênis", variable=checkbox_value_b)

for value in data:
    listbox.insert(END, value)

def click():
    global times

    label.configure(text=f"Botão foi clicado {times} vezes!", font=("Arial", 16))

    times += 1

button = Button(window, text="Clique aqui!", command=click)

def show_label(event):
    label.pack()

# label.place(x=60, y=10)
# textbox.place(x=60, y=40)
# combobox.place(x=60, y=80)
# listbox.place(x=60, y=130)
# button.place(x=60, y=200)
# radio_a.place(x=50, y=50)
# radio_b.place(x=150, y=50)
checkbox_a.place(x=50, y=50)
checkbox_a.bind('<Button-1>', show_label)

checkbox_b.place(x=150, y=50)

window.mainloop()