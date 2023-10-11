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

    label = Label(venster, text="Kies uw ras")
    label.place(anchor= 'center', relx= 0.5, rely= 0.45)


    elf_foto = PhotoImage(file='images/ELF_character.png')
    ras_kiezen_button_elf = Label(image=elf_foto)
    ras_kiezen_button_elf.pack()

    # ras_kiezen_button_dwerg  =
    #
    # ras_kiezen_button_hobbit =
    #
    # ras_kiezen_button_mens =




