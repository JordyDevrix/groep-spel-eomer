
def verhaal_kiezen():
    with open("verhaal.json", "r") as verhaal_json:
        verhaal_keuze = input(f"Welkom bij de middel aarde verhaal game.\nkies uw verhaal\n1.  {verhaal_json['1']['verhaal_naam']}\n2.   {verhaal_json['2']['verhaal_naam']}\n3.   {verhaal_json['3']['verhaal_naam']}")
        for verhaal in verhaal_json:
            if verhaal_keuze == verhaal_json["verhaal_naam"]:
                return verhaal
            else:
                None
        print("Uw invoer was niet geldig probeer het opnieuw.")
        return verhaal_kiezen()

