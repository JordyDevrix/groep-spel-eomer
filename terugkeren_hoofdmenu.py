import keyboard

def scan_toetsenbord():
    keyboard.read_key()

def terug_keren_naar_menu():
    speler_keuze = input("Weet je zeker dat je wilt stoppen en wilt terugkeren naar het hoofdmenu? (Y or N)")

    if speler_keuze == "Y":
        print("Hier wordt de functie 'hoofdmenu tonen' aangeroepen.")
    elif speler_keuze == "N":
        print("Hier gaat het programma verder waar het gebleven was.")
    else:
        print("Ongeldige invoer")
        terug_keren_naar_menu()

keyboard.add_hotkey('esc', terug_keren_naar_menu)

while True:
    scan_toetsenbord()