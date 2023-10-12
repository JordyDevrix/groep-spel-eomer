import json
import tkinter as tk


class TekstAvontuur:
    def __init__(self, root, gegevensbestand):
        self.gegevens = lees_gegevens(gegevensbestand)
        self.huidige_locatie = "start"

        root.title("Tekstavontuur")
        root.geometry("1400x800")


        top_bar = tk.Frame(root, bg="grey", height=40)
        top_bar.pack(fill="both")

        self.beschrijving_label = tk.Label(root, justify="left", text="", wraplength=800, padx=10, pady=10)
        self.beschrijving_label.place(anchor="center", relx=0.5, rely=0.9)

        self.button_frame = tk.Frame(root)
        self.button_frame.place(anchor="center", relx=0.5, rely=0.5)

        self.keuze_buttons = []

        self.update_interface()

        root.mainloop()

    def update_interface(self):
        het_ras_van_de_speler_is_mens = False
        het_ras_van_de_speler_is_dwerg = True

        locatie_data = self.gegevens["locaties"][self.huidige_locatie]
        self.beschrijving_label.config(text=locatie_data["beschrijving"])

        for button in self.keuze_buttons:
            button.destroy()

        keuzes = locatie_data["keuzes"]

        for i, keuze in enumerate(keuzes):
            keuze_text = list(keuze.keys())[0]
            nieuwe_locatie = list(keuze.values())[0]

            if "Dwerg" in keuze_text:
                if het_ras_van_de_speler_is_dwerg:
                    button = tk.Button(self.button_frame, width=47, height=30, bg="grey", text=keuze_text,
                                       command=lambda loc=nieuwe_locatie: self.kies_optie(loc))
                    button.grid(padx=20, pady=5, column=i, row=0)
                    self.keuze_buttons.append(button)
            elif "Mens" in keuze_text:
                if het_ras_van_de_speler_is_mens:
                    button = tk.Button(self.button_frame, width=47, height=30, bg="grey", text=keuze_text,
                                       command=lambda loc=nieuwe_locatie: self.kies_optie(loc))
                    button.grid(padx=20, pady=5, column=i, row=0)
                    self.keuze_buttons.append(button)
            else:
                button = tk.Button(self.button_frame, width=47, height=30, bg="grey", text=keuze_text,
                                   command=lambda loc=nieuwe_locatie: self.kies_optie(loc))
                button.grid(padx=20, pady=5, column=i, row=0)
                self.keuze_buttons.append(button)

    def kies_optie(self, nieuwe_locatie):
        self.huidige_locatie = nieuwe_locatie
        if nieuwe_locatie is not None:
            self.update_interface()
        else:
            self.beschrijving_label.config(text="Tot ziens!")
            for button in self.keuze_buttons:
                button.destroy()


def lees_gegevens(gegevensbestand):
    with open(gegevensbestand, 'r') as bestand:
        return json.load(bestand)


def start_tekst_avontuur(root):
    for widget in root.winfo_children():
        widget.destroy()
    TekstAvontuur(root, "files/avontuurgegevens.json")


if __name__ == "__main__":
    start_tekst_avontuur()