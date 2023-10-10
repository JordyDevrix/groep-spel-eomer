from tkinter import *

def hoofdmenu():
    root = Tk()
    root.geometry("500x500")
    root.title("Hoofdmenu")

    label = Label(root, text="Welkom bij Lord of the Rings Legends")
    label.pack()

    button = Button(root, text="Speel",
                    font=("Arial", 24),
                    command=lambda : scherm_speel(root))
    button.pack()



    root.mainloop()

def scherm_speel(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = Label(root, text="Hallo")
    label.grid(column = 0, row = 0)

    labl = Label(root, text="Hallo")
    labl.grid(column=1, row=1)
#

#
    root.mainloop()