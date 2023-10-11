from tkinter import *

def main(root):
    for widget in root.winfo_children():
        widget.destroy()

    button_tl = Button(root, text= "Tijd/Locatie", command= lambda: tijd_locatie_weergeven(root))
    button_tl.place(x=20, y=750)

    root.mainloop()


def tijd_locatie_weergeven(root):
    for widget in root.winfo_children():
        widget.destroy()

    tijd= "10:12"
    locatie= "Rivendel"

    lt_label = Label(root, text=f"{tijd} en {locatie}", font="Roboto, 24")
    lt_label.place(x=520, y=350)
    close_button = Button(root, text= "x", command=lambda: main(root))
    close_button.place(x=700, y=420)




if __name__ == '__main__':
    root = Tk()
    root.geometry("1400x800")
    main(root)
