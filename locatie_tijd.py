from tkinter import *


def main(root):
    for widget in root.winfo_children():
        widget.destroy()

    button_tl = Button(root, text="Tijd/Locatie", command=lambda: tijd_locatie_weergeven(root))
    button_tl.place(x=20, y=750)

    root.mainloop()


def tijd_locatie_weergeven(root):

    tijd = "10:12"
    locatie = "Rivendel"

    frame1 = Frame(root, width=300, height=120, highlightbackground="blue", highlightthickness=6)
    frame1.place(x=600, y=340)

    lt_label = Label(frame1, text=f"{tijd} en {locatie}", font=("Roboto", 24))
    lt_label.grid(row=0, column=0, pady=20)  # Center label vertically

    close_button = Button(frame1, text="x", command=lambda: main(root))
    close_button.grid(row=1, column=0)

