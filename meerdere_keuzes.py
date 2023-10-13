import json
import tkinter as tk


gemaakte_keuzes = []
het_ras_van_de_speler_is_mens = False
het_ras_van_de_speler_is_dwerg = False


def lees_gegevens(gegevensbestand):
    with open(gegevensbestand, 'r', encoding='utf-8') as bestand:
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
                button = tk.Button(button_frame, width=35, height=15, bg="grey", text=keuze_text, font="Roboto,18",
                                   command=lambda loc=nieuwe_locatie:
                                   kies_optie(loc, huidige_locatie, gegevens, beschrijving_label, button_frame))
                button.grid(padx=20, pady=5, column=i, row=0)
        elif "Mens" in keuze_text:
            if het_ras_van_de_speler_is_mens:
                button = tk.Button(button_frame, width=35, height=15, bg="grey", text=keuze_text, font="Roboto,18",
                                   command=lambda loc=nieuwe_locatie:
                                   kies_optie(loc, huidige_locatie, gegevens, beschrijving_label, button_frame))
                button.grid(padx=20, pady=5, column=i, row=0)
        else:
            button = tk.Button(button_frame, width=35, height=15, bg="grey", text=keuze_text, font="Roboto,18",
                               command=lambda loc=nieuwe_locatie:
                               kies_optie(loc, huidige_locatie, gegevens, beschrijving_label, button_frame))
            button.grid(padx=20, pady=5, column=i, row=0)


def tijd_locatie_weergeven(huidige_locatie):

    locatie = huidige_locatie

    frame1 = tk.Frame(width=300, height=120, highlightbackground="blue", highlightthickness=6)
    frame1.place(anchor="center", relx=0.5, rely=0.5)

    lt_label = tk.Label(frame1, text=f"{locatie}", font=("Roboto", 24))
    lt_label.grid(row=0, column=0, pady=20)  # Center label vertically
    close_button = tk.Button(frame1, text="x",
                             command=lambda: (close_button.destroy(), lt_label.destroy(), frame1.destroy()))
    close_button.grid(row=1, column=0)


def kies_optie(nieuwe_locatie, huidige_locatie, gegevens, beschrijving_label, button_frame):
    locatie_data = gegevens["locaties"][huidige_locatie]
    keuzes = locatie_data["keuzes"]
    geselecteerde_keuze = next((keuze for keuze in keuzes if list(keuze.values())[0] == nieuwe_locatie), None)
    button_tl = tk.Button(text="Actie/Locatie", command=lambda: tijd_locatie_weergeven(huidige_locatie))
    button_tl.place(x=20, y=750)
    if geselecteerde_keuze:
        geselecteerde_keuze_tekst = list(geselecteerde_keuze.keys())[0]
        gemaakte_keuzes.append(geselecteerde_keuze_tekst)

    huidige_locatie = nieuwe_locatie

    if nieuwe_locatie is not None:
        update_interface(huidige_locatie, gegevens, beschrijving_label, button_frame)
    else:
        gemaakte_keuzes_tekst = "\n- ".join(gemaakte_keuzes)
        beschrijving_label.place_forget()
        button_frame.place_forget()
        gemaakte_keuzes_label = tk.Label(justify="center", font="Roboto, 12", text=gemaakte_keuzes_tekst,
                                         wraplength=800, padx=10, pady=10)
        gemaakte_keuzes_label.place(anchor="center", relx=0.5, rely=0.5)
        gemaakte_keuzes.clear()

        for knop in button_frame.winfo_children():
            knop.destroy()
    tk.mainloop()


def start_tekst_avontuur(root, bestand, menu):

    gegevens = lees_gegevens(bestand)

    for widget in root.winfo_children():
        widget.destroy()

    huidige_locatie = "start"

    root.geometry("1400x800")

    for widget in root.winfo_children():
        widget.destroy()
    bg_image = tk.PhotoImage(file="images/Mordor background.png")

    bg_image = bg_image.zoom(10)
    bg_image = bg_image.subsample(7)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0)
    button_frame = tk.Frame(root)
    button_frame.place(anchor="center", relx=0.5, rely=0.5)
    top_bar = tk.Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")
    cancel_button = tk.Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")

    beschrijving_label = tk.Label(root, justify="center", font="Roboto, 12", text="", wraplength=800, padx=10, pady=10)
    beschrijving_label.place(anchor="center", relx=0.5, rely=0.15)

    button_frame = tk.Frame(root, bg='darkred')
    button_frame.place(anchor="center", relx=0.5, rely=0.5)

    update_interface(huidige_locatie, gegevens, beschrijving_label, button_frame)
    tk.mainloop()
