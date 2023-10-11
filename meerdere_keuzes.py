import json


def lees_gegevens(gegevensbestand):
    with open(gegevensbestand, 'r') as f:
        gegevens = json.load(f)
    return gegevens


def speel(gegevens):
    huidige_locatie = "start"

    print("Welkom bij het tekstavontuur!")

    while True:
        locatie_data = gegevens["locaties"][huidige_locatie]
        print("\n" + locatie_data["beschrijving"])
        keuzes = locatie_data["keuzes"]

        if not keuzes:
            print("Dit is het einde van het avontuur.")
            break

        print("Beschikbare keuzes:")
        for i, keuze in enumerate(keuzes):
            print(f"{i + 1}. {list(keuze.keys())[0]}")

        keuze_nummer = input("Voer het nummer van je keuze in: ")
        try:
            keuze_nummer = int(keuze_nummer)
            if 1 <= keuze_nummer <= len(keuzes):
                nieuwe_locatie = list(keuzes[keuze_nummer - 1].values())[0]
                if nieuwe_locatie is not None:
                    huidige_locatie = nieuwe_locatie
                else:
                    print("Tot ziens!")
                    break
            else:
                print("Ongeldige keuze. Probeer opnieuw.")
        except ValueError:
            print("Ongeldige invoer. Voer het nummer van je keuze in.")


# if __name__ == "__main__":
#     gegevens = lees_gegevens("files/avontuurgegevens.json")
#     speel(gegevens)