import json
import tkinter as tk

gemaakte_keuzes = []
het_ras_van_de_speler_is_mens = False
het_ras_van_de_speler_is_dwerg = False

def lees_gegevens(gegevensbestand):
    with open(gegevensbestand, 'r') as bestand:
        return json.load(bestand)


def update_interface(huidige_locatie, gegevens, beschrijving_label, button_frame):
    locatie_data = gegevens["locaties"][huidige_locatie]
    beschrijving_label.config(text=locatie_data["beschrijving"])

    for button in button_frame.winfo_children():
        button.destroy()

    keuzes = locatie_data["keuzes"]

    for i, keuze in enumerate(keuzes):
        keuze_text = list(keuze.keys())[0]
        nieuwe_locatie = list(keuze.values())[0]

        if "Dwerg" in keuze_text:
            if het_ras_van_de_speler_is_dwerg:
                button = tk.Button(button_frame, width=47, height=30, bg="grey", text=keuze_text,
                                   command=lambda loc=nieuwe_locatie: kies_optie(loc, huidige_locatie, gegevens, beschrijving_label, button_frame))
                button.grid(padx=20, pady=5, column=i, row=0)
        elif "Mens" in keuze_text:
            if het_ras_van_de_speler_is_mens:
                button = tk.Button(button_frame, width=47, height=30, bg="grey", text=keuze_text,
                                   command=lambda loc=nieuwe_locatie: kies_optie(loc, huidige_locatie, gegevens, beschrijving_label, button_frame))
                button.grid(padx=20, pady=5, column=i, row=0)
        else:
            button = tk.Button(button_frame, width=47, height=30, bg="grey", text=keuze_text,
                               command=lambda loc=nieuwe_locatie: kies_optie(loc, huidige_locatie, gegevens, beschrijving_label, button_frame))
            button.grid(padx=20, pady=5, column=i, row=0)


def kies_optie(nieuwe_locatie, huidige_locatie, gegevens, beschrijving_label, button_frame):
    locatie_data = gegevens["locaties"][huidige_locatie]
    keuzes = locatie_data["keuzes"]
    keuze_text = [list(keuze.keys())[0] for keuze in keuzes if list(keuze.values())[0] == nieuwe_locatie][0]
    gemaakte_keuzes.append(keuze_text)

    huidige_locatie = nieuwe_locatie
    if nieuwe_locatie is not None:
        update_interface(huidige_locatie, gegevens, beschrijving_label, button_frame)
    else:
        for button in button_frame.winfo_children():
            beschrijving_label.config(text=gemaakte_keuzes)
            button.destroy()


def start_tekst_avontuur(root, bestand, menu):

    gegevens = lees_gegevens(bestand)

    for widget in root.winfo_children():
        widget.destroy()

    bg_image = tk.PhotoImage(file="images/Lord of the rings background (1).png")
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0)

    huidige_locatie = "start"

    root.title("Tekstavontuur")
    root.geometry("1400x800")

    for widget in root.winfo_children():
        widget.destroy()

    top_bar = tk.Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = tk.Button(top_bar, width=3, height=1, text="X", command=lambda : menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")

    beschrijving_label = tk.Label(root, justify="left", text="", wraplength=800, padx=10, pady=10)
    beschrijving_label.place(anchor="center", relx=0.5, rely=0.9)

    button_frame = tk.Frame(root)
    button_frame.place(anchor="center", relx=0.5, rely=0.5)

    update_interface(huidige_locatie, gegevens, beschrijving_label, button_frame)


