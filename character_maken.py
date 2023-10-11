import json
import tkinter
from tkinter import *

from PIL import Image, ImageTk






def character_wegschrijven():
    name = input()
    with open(f"charater_{name}.json", 'w') as bestand:
        gegevens = {
            "ras": 'Dwerg',
            "naam": name
        }
        data = json.dumps(gegevens, indent=1)
        bestand.write(data)
    return  name


def character_ophalen(name):

    with open(f"charater_{name}.json", 'r') as bestand:
        data = json.load(bestand)
        print(data)





def character_maken(venster, menu):
    for widget in venster.winfo_children():
        widget.destroy()

    top_bar = Frame(venster, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(venster))
    cancel_button.pack(padx=5, pady=5, side="right")

    naam_input_frame = Frame(venster)
    naam_input_frame.place(anchor='center', relx=0.5, rely=0.5)

    label = Label(naam_input_frame, text="Vul uw naam in ", font="Roboto, 24")
    label.grid(row=0, column=0)

    name_input = Entry(naam_input_frame, width=10, font="Roboto, 24")
    name_input.grid(row=0, column=1)

    haal_naam_op_knop = Button(naam_input_frame, text="Haal tekst op", command=lambda: naam_ophalen(venster, name_input))
    haal_naam_op_knop.grid(row=0, column=2)

    return venster




def naam_ophalen(venster, name_input):
    name_inhoud = name_input.get()
    name_input.delete(0, tkinter.END)
    name = name_inhoud
    label_huidge_naam = Label(venster, text= f"Uw huidige naam: {name}")
    label_huidge_naam.place(anchor= 'center', relx= 0.5, rely=0.65)
    doorgaan_button = Button(venster, text="Ga door naar volgende keuze.", font=("Arial, 10"), command=lambda : ras_kiezen(venster))
    doorgaan_button.place(anchor= 'center', relx= 0.5, rely= 0.6)

def ras_kiezen(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    frame = Frame(venster)

    # Laden van afbeeldingen
    dwerg_image = Image.open("images/dwerg.png")
    mens_image = Image.open('images/mens.png')

    # Schalen van de afbeeldingen
    dwerg_image = dwerg_image.resize((250, 500))
    mens_image = mens_image.resize((250, 500))

    # Omzetten naar een formaat dat tkinter kan gebruiken
    venster.dwerg_photo = ImageTk.PhotoImage(dwerg_image)
    venster.mens_photo = ImageTk.PhotoImage(mens_image)

    # Knoppen maken met afbeeldingen
    dwerg_button = Button(venster, image=venster.dwerg_photo, command=lambda: ras_binnen_krijgen(venster, 1))
    dwerg_button.place(anchor='center', relx=0.25, rely=0.4)

    mens_button = Button(venster, image=venster.mens_photo, command=lambda: ras_binnen_krijgen(venster, 2))
    mens_button.place(anchor='center', relx=0.75, rely=0.4)

    frame.pack()

    tekst_dwerg = Label(venster, text="Dwerg", font=("Roboto, 24"))
    tekst_dwerg.place(anchor='center', relx=0.25, rely=0.75)

    tekst_mens = Label(venster, text="Mens", font=("Roboto, 24"))
    tekst_mens.place(anchor='center', relx=0.75, rely=0.75)

    tekst_mens_beschrijving = Label(venster, text="Eigenschap: Slim", font=("Roboto, 24"))
    tekst_mens_beschrijving.place(anchor='center', relx=0.75, rely=0.8)

    tekst_dwerg_beschrijving = Label(venster, text="Eigenschap: Sterk", font=("Roboto, 24"))
    tekst_dwerg_beschrijving.place(anchor='center', relx=0.25, rely=0.8)

    tekst = Label(venster, text="Kies uw Ras", font=('Roboto, 24'))
    tekst.pack()



def ras_binnen_krijgen(venster, type_ras):
    for widget in venster.winfo_children():
        widget.destroy()

    if type_ras == 1:
        eigenschap = "sterk"
    elif type_ras == 2:
        eigenschap = "slim"

    label = Label(venster, text="Je hebt een character!", font=("Roboto, 24"))
    label.place(anchor= 'center', relx=0.5, rely=0.4)

    top_bar = Frame(venster, bg="grey", height=40)
    top_bar.pack(fill="both")
    from app_gui import menu
    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(venster))
    cancel_button.place()