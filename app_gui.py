from tkinter import *
from admin_inloggen import *
from character_maken import character_maken

# def character(root):
#     for widget in root.winfo_children():
#         widget.destroy()
#
#     top_bar = Frame(root, bg="grey", height=40)
#     top_bar.pack(fill="both")
#
#
#
#     char = Frame(root)
#     char.pack()
#     cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
#     cancel_button.pack(padx=5, pady=5, side="right")


def settings(root):
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    char = Frame(root)
    char.pack()
    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")


def spel_spelen(root):
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    avonturen_frame = Frame(root)
    avonturen_frame.place(anchor="center", relx=0.5, rely=0.5)

    avontuur_een = Frame(avonturen_frame, width=400, height=700, bg="grey")
    avontuur_een.grid(padx=20, pady=5, column=0, row=0)

    avontuur_twee = Frame(avonturen_frame, width=400, height=700, bg="grey")
    avontuur_twee.grid(padx=20, pady=5, column=1, row=0)

    avontuur_drie = Frame(avonturen_frame, width=400, height=700, bg="grey")
    avontuur_drie.grid(padx=20, pady=5, column=2, row=0)

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")



def menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    menu_frame = Frame(root, bg="grey")
    menu_frame.pack(fill="both", expand=True, padx=5, pady=5)

    menu_button_frame = Frame(menu_frame, height=200, width=400, bg="red")
    menu_button_frame.place(anchor="center", relx=0.5, rely=0.5)
    maak_character = Button(menu_button_frame,
                            text="CREATE A CHARACTER",
                            font="Roboto, 20",
                            width=40,
                            command=lambda: character_maken(root, menu))
    maak_character.pack(padx=10, pady=10, fill="both")

    speel_spel = Button(menu_button_frame,
                        text="PLAY GAME",
                        font="Roboto, 20",
                        width=40,
                        command=lambda: spel_spelen(root))
    speel_spel.pack(padx=10, pady=10, fill="both")

    settings_optie = Button(menu_button_frame,
                            text="SETTINGS",
                            font="Roboto, 20",
                            width=40,
                            command=lambda: settings(root))
    settings_optie.pack(padx=10, pady=10, fill="both")

    admin_opties = Button(menu_button_frame,
                            text="ADMIN MODE",
                            font="Roboto, 20",
                            width=40,
                            command=lambda: admin_inlogscherm(root, menu))
    admin_opties.pack(padx=10, pady=10, fill="both")


def applicatie_gui():

    root = Tk()
    root.geometry("1400x800")

    app_frame = Frame(root)
    app_frame.pack(fill="both", expand=True)

    menu(app_frame)



    root.mainloop()


applicatie_gui()
