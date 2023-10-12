from tkinter import *
import meerdere_keuzes as mk


def verhaal_kiezen(root, menu):

    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")

    avonturen_frame = Frame(root)
    avonturen_frame.place(anchor="center", relx=0.5, rely=0.5)

    avontuur_een = Button(root ,text="Avontuur naar",width=50, height=30, command=lambda: mk.start_tekst_avontuur(root, "files/avontuurgegevens.json"))
    avontuur_een.place(anchor='center', relx=0.25, rely=0.5)

    avontuur_twee = Button(root, text="Hey", width=50, height=30, command=lambda: mk.start_tekst_avontuur(root, "files/avontuurgegevens_2.json"))
    avontuur_twee.place(anchor='center', relx=0.50, rely=0.5)

    avontuur_drie = Button(root, text="hallo ",width=50, height=30, command=lambda: mk.start_tekst_avontuur(root, "files/avontuurgegevens.json"))
    avontuur_drie.place(anchor='center', relx=0.75, rely=0.5)
