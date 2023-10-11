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





def character_maken(venster):
    for widget in venster.winfo_children():
        widget.destroy()


    naam_input_frame = Frame(venster)
    naam_input_frame.place(anchor= 'center', relx= 0.5, rely= 0.5)

    label = Label(naam_input_frame, text="Vul uw naam in.", font="Roboto, 24")
    label.pack()

    name_input = Entry(naam_input_frame, width=10, font="Roboto, 24")
    name_input.pack()

    haal_naam_op_knop = Button(venster, text="Haal tekst op", command= lambda : naam_ophalen(venster, name_input))
    haal_naam_op_knop.pack()





def naam_ophalen(venster, name_input):
    name_inhoud = name_input.get()
    name_input.delete(0, tkinter.END)
    name = name_inhoud
    label_huidge_naam = Label(venster, text= f"Uw huidige naam: {name}")
    label_huidge_naam.place(anchor= 'center', relx= 0.5, rely=0.6)
    doorgaan_button = Button(venster, text="Ga door naar volgende keuze.", font=("Arial, 10"), command=lambda : ras_kiezen(venster))
    doorgaan_button.place(anchor= 'center', relx= 0.5, rely= 0.56)

def ras_kiezen(venster):
    for widget in venster.winfo_children():
        widget.destroy()

    label = Label(venster, text="HEY")
    label.pack()

def main_charac(root):
    for widget in root.winfo_children():
        widget.destroy()

    button_charac_maken = Button(root, text="Character maken", font=("Arial",24), command=lambda : character_maken(root))
    button_charac_maken.pack()

    name = character_wegschrijven()
    character_ophalen(name)


