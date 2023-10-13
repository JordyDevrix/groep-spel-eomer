from tkinter import *
import meerdere_keuzes as mk
from PIL import Image, ImageTk


def verhaal_kiezen(root, menu):
    for widget in root.winfo_children():
        widget.destroy()
    bg_image = PhotoImage(file="images/Character_kies_achtegrond-transformed (1).png")
    bg_label = Label(root, image=bg_image)
    bg_label.place(x=0, y=0)
    avontuur_1_foto = Image.open('images/isengard.jpg')
    avontuur_2_foto = Image.open('images/MysteryForest.jpg')
    avontuur_3_foto = Image.open('images/ittilen.jpg')

    avontuur_1_foto = avontuur_1_foto.resize((300, 500))
    avontuur_2_foto = avontuur_2_foto.resize((300, 500))
    avontuur_3_foto = avontuur_3_foto.resize((300, 500))

    root.avontuur_1_foto = ImageTk.PhotoImage(avontuur_1_foto)
    root.avontuur_2_foto = ImageTk.PhotoImage(avontuur_2_foto)
    root.avontuur_3_foto = ImageTk.PhotoImage(avontuur_3_foto)

    tekst_verhaal_een = Label(root, text="Saruman's plan", font="Roboto, 24")
    tekst_verhaal_een.place(anchor= 'center', relx= 0.24, rely= 0.85)

    tekst_verhaal_een = Label(root, text="De Entwives Zoektocht ", font="Roboto, 24")
    tekst_verhaal_een.place(anchor='center', relx=0.50, rely=0.85)

    tekst_verhaal_een = Label(root, text="Het avontuur van Ithlien ", font="Roboto, 24")
    tekst_verhaal_een.place(anchor='center', relx=0.75, rely=0.85)

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")

    avonturen_frame = Frame(root)
    avonturen_frame.place(anchor="center", relx=0.5, rely=0.5)

    avontuur_een = Button(root, text="Avontuur naar", image=root.avontuur_1_foto,
                          command=lambda: mk.start_tekst_avontuur(root, "files/avontuurgegevens.json", menu))
    avontuur_een.place(anchor='center', relx=0.25, rely=0.5)

    avontuur_twee = Button(root, text="Hey",image=root.avontuur_2_foto,
                           command=lambda: mk.start_tekst_avontuur(root, "files/avontuurgegevens_2.json", menu))
    avontuur_twee.place(anchor='center', relx=0.50, rely=0.5)

    avontuur_drie = Button(root, text="hallo ",image=root.avontuur_3_foto,
                           command=lambda: mk.start_tekst_avontuur(root, "files/avontuurgegevens_3.json", menu))
    avontuur_drie.place(anchor='center', relx=0.75, rely=0.5)
    root.mainloop()