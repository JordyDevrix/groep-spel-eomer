import json
import tkinter
import meerdere_keuzes as mk
from tkinter import *
from PIL import Image, ImageTk


def character_maken(venster: Tk, menu):
    for widget in venster.winfo_children():
        widget.destroy()

    bg_image = PhotoImage(file="images/Character_kies_achtegrond-transformed (1).png")

    # ================================ # maakt achtergrond resizable
    bg_image = bg_image.zoom(10)
    bg_image = bg_image.subsample(7)
    # ================================ #
    bg_label = Label(venster, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    top_bar = Frame(venster, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(venster))
    cancel_button.pack(padx=5, pady=5, side="right")

    naam_input_frame = Frame(venster, width=400, height=250, bd=2, relief="solid", highlightthickness=1, highlightbackground="black")

    naam_input_frame.place(anchor='center', relx=0.5, rely=0.5)

    label = Label(naam_input_frame, text="Vul uw naam in ", font="Roboto, 24")
    label.pack()

    name_input = Entry(naam_input_frame, width=10, font="Roboto, 24")
    name_input.pack()

    haal_naam_op_knop = Button(naam_input_frame, text="Klaar",width=4,height=2 ,command=lambda: naam_ophalen(venster, name_input, menu))
    haal_naam_op_knop.pack()

    venster.mainloop()

    return venster


def character_ophalen(name):
    with open(f"charater_{name}.json", 'r') as bestand:
        data = json.load(bestand)
        print(data)


def naam_ophalen(venster, name_input, menu):
    naam_character = name_input.get()
    bg_image = PhotoImage(file="images/Character_kies_achtegrond-transformed (1).png")

    # ================================ # maakt achtergrond resizable
    bg_image = bg_image.zoom(10)
    bg_image = bg_image.subsample(7)
    # ================================ #

    bg_label = Label(venster, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    if naam_character == "" or naam_character == " ":

        character_maken(venster, menu)
        label = Label(venster, text="Dit is niet geldig", font="Roboto, 24")
        label.pack()
    elif naam_character == "Frodo Baggings":
        label = Label(venster, text="It must often be so, Sam, when things are in danger: some one has to "
                                    "give them up, lose them, so that others may keep them", font="Roboto, 16")
        label.pack()

    elif naam_character == "Vincent" or naam_character == 'vincent' or naam_character == 'Vincent Spijkers':
        label_vincent = Label(venster, text="Legend!", font="CheapFire, 24")
        label_vincent.pack()
    name_input.delete(0, tkinter.END)

    label_huidge_naam = Label(venster, text= f"Uw gekozen naam: {naam_character}", font="Roboto, 17")
    label_huidge_naam.place(anchor= 'center', relx= 0.5, rely=0.65)
    doorgaan_button = Button(venster, text="Ga door naar volgende keuze.", font="Roboto, 18",
                                    command=lambda : ras_kiezen(venster, menu, naam_character))
    doorgaan_button.place(anchor= 'center', relx= 0.5, rely= 0.5)

    venster.mainloop()



def ras_kiezen(venster, menu, name_inhoud):
    for widget in venster.winfo_children():
        widget.destroy()
    bg_image = PhotoImage(file="images/Character_kies_achtegrond-transformed (1).png")

    # ================================ # maakt achtergrond resizable
    bg_image = bg_image.zoom(10)
    bg_image = bg_image.subsample(7)
    # ================================ #

    bg_label = Label(venster, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    frame = Frame(venster)

    top_bar = Frame(venster, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(venster))
    cancel_button.pack(padx=5, pady=5, side="right")

    dwerg_image = Image.open("images/dwerg.png")
    mens_image = Image.open('images/mens.png')

    dwerg_image = dwerg_image.resize((300, 500))
    mens_image = mens_image.resize((300, 500))

    venster.dwerg_photo = ImageTk.PhotoImage(dwerg_image)
    venster.mens_photo = ImageTk.PhotoImage(mens_image)

    dwerg_button = Button(venster, image=venster.dwerg_photo, command=lambda: ras_binnen_krijgen(venster, 1, menu, name_inhoud))
    dwerg_button.place(anchor='center', relx=0.25, rely=0.4)

    mens_button = Button(venster, image=venster.mens_photo, command=lambda: ras_binnen_krijgen(venster, 2, menu, name_inhoud))
    mens_button.place(anchor='center', relx=0.75, rely=0.4)

    frame.pack()

    tekst_dwerg = Label(venster, text="Dwerg", font="Roboto, 24")
    tekst_dwerg.place(anchor='center', relx=0.25, rely=0.75)

    tekst_mens = Label(venster, text="Mens", font="Roboto, 24")
    tekst_mens.place(anchor='center', relx=0.75, rely=0.75)

    tekst_mens_eigenschap = Label(venster, text="Eigenschap: Slim", font="Roboto, 24")
    tekst_mens_eigenschap.place(anchor='center', relx=0.75, rely=0.8)

    tekst_dwerg_eigenschap = Label(venster, text="Eigenschap: Sterk", font="Roboto, 24")
    tekst_dwerg_eigenschap.place(anchor='center', relx=0.25, rely=0.8)

    tekst = Label(venster, text="Kies uw Ras", font='Roboto, 24')
    tekst.pack()
    venster.mainloop()


def ras_binnen_krijgen(venster, type_ras, menu, name_inhoud):

    from spel_spelen_functie import verhaal_kiezen

    for widget in venster.winfo_children():
        widget.destroy()

    if type_ras == 1:
        ras = "dwerg (sterk)"
        mk.het_ras_van_de_speler_is_dwerg = True
        mk.het_ras_van_de_speler_is_mens = False
    else:
        ras = "mens (slim)"
        mk.het_ras_van_de_speler_is_mens = True
        mk.het_ras_van_de_speler_is_dwerg = False

    bg_image = PhotoImage(file="images/Character_kies_achtegrond-transformed (1).png")

    # ================================ # maakt achtergrond resizable
    bg_image = bg_image.zoom(10)
    bg_image = bg_image.subsample(7)
    # ================================ #

    bg_label = Label(venster, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)
    label_je_hebt_een_character = Label(venster, text="Je hebt een character!", font="Roboto, 24")
    label_je_hebt_een_character.place(anchor= 'center', relx=0.5, rely=0.4)
    doorgaan_naar_kiezen_verhaal = Button(venster,width=12, height=1 ,text="Verhaal kiezen", font="Roboto, 24", command=lambda : verhaal_kiezen(venster, menu))
    doorgaan_naar_kiezen_verhaal.place(anchor='center', relx=0.5, rely=0.5)

    top_bar = Frame(venster, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=5, height=3, text="X", command=lambda: menu(venster))
    cancel_button.place(anchor= 'center', relx=0.5, rely=0.5)

    character_gegevens_wegschrijven(ras, name_inhoud)
    venster.mainloop()


def character_gegevens_wegschrijven(ras, name_input):

    with open(f"charater_gegevens.json", 'w') as bestand:
        gegevens = {
            "Ras": ras,
            "naam": str(name_input)
        }
        data = json.dumps(gegevens, indent=1)
        bestand.write(data)




