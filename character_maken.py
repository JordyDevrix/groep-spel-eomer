import json
import tkinter
from tkinter import *






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

    naam_input_frame = Frame(venster, borderwidth=5, relief="solid", padx=15, pady=15)
    naam_input_frame.place(anchor='center', relx=0.5, rely=0.5)

    label = Label(naam_input_frame, text="Vul uw naam in.", font="Roboto, 24")
    label.pack()

    name_input = Entry(naam_input_frame, width=10, font="Roboto, 24")
    name_input.pack()

    haal_naam_op_knop = Button(venster, text="Haal tekst op", command=lambda: naam_ophalen(venster, name_input))
    haal_naam_op_knop.pack()
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

    label = Label(venster, text="HEY")
    label.pack()



