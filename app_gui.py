from tkinter import *


def karakter(root):
    char = Frame(root)
    char.pack()
    abutton = Button(char)
    abutton.pack()


def applicatie_gui():
    root = Tk()
    root.geometry("1400x800")

    app_frame = Frame(root)
    app_frame.pack(fill="both", expand=True)

    menu_frame = Frame(app_frame, bg="grey")
    menu_frame.pack(fill="both", expand=True, padx=5, pady=5)

    second_button = Button(menu_frame, text="hello", command=lambda: karakter(root))
    second_button.pack()

    root.mainloop()


applicatie_gui()
