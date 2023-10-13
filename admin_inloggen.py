from tkinter import *
import json


def check_inlog(input_gebruikersnaam, input_wachtwoord, root, menu):
    with open("files/admin_inlog.json") as bestand:
        inhoud = json.load(bestand)
    if input_gebruikersnaam == inhoud['gebruikersnaam'] and input_wachtwoord == inhoud['wachtwoord']:
        print("Ingelogd")
        admin_scherm(root, menu)


def admin_inlogscherm(root, menu):
    for widget in root.winfo_children():
        widget.destroy()
    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command= lambda : menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")

    frame = Frame(root, bg="#ded9ee")
    frame.pack(fill="both", expand=True)

    titel = Label(frame, text="Admin login", font=("Roboto", 24), bg="#ded9ee")
    titel.pack(padx= 25, pady= 25)

    admin_login_frame = Frame(frame, bg="#ded9ee")
    admin_login_frame.place(anchor="center", relx=0.5, rely=0.5)

    gebruikersnaam_label = Label(admin_login_frame, text="Gebruikersnaam", bg="#ded9ee")
    input_gebruikersnaam = Entry(admin_login_frame, bd=5)

    wachtwoord_label = Label(admin_login_frame, text="Wachtwoord", bg="#ded9ee")
    input_wachtwoord = Entry(admin_login_frame, bd=5, show="*")

    inlog_button = Button(admin_login_frame, width=25, height=2, text="Log in",
                          command=lambda: check_inlog(input_gebruikersnaam.get(),
                                                      input_wachtwoord.get(),
                                                      root,
                                                      menu))

    gebruikersnaam_label.pack(padx=5, pady=5)
    input_gebruikersnaam.pack(padx=5, pady=5)
    wachtwoord_label.pack(padx=5, pady=5)
    input_wachtwoord.pack(padx=5, pady=5)
    inlog_button.pack(padx=5, pady=5)

    return root, menu


def admin_scherm(root, menu):
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")
    frame = Frame(root, bg="#ded9ee")
    frame.pack(fill="both", expand=True)
    titel = Label(frame, text="Admin portaal", font=("Roboto", 24), bg="#ded9ee")
    titel.pack(padx=25, pady=25)

    verhaal_button_frame = Frame(frame, height=650, width=500, bg="#ded9ee")
    verhaal_button_frame.place(anchor="center", relx=0.5, rely=0.5)

    admin_verhaal_1 = Button(verhaal_button_frame,
                          text="Verhaal 1",
                          font="Roboto, 20",
                          width=40,
                          command=lambda: verhaal_1(root, menu))
    admin_verhaal_2 = Button(verhaal_button_frame,
                          text="Verhaal 2",
                          font="Roboto, 20",
                          width=40,
                          command=lambda: verhaal_2(root, menu))
    admin_verhaal_3 = Button(verhaal_button_frame,
                          text="Verhaal 3",
                          font="Roboto, 20",
                          width=40,
                          command=lambda: verhaal_3(root, menu))
    admin_verhaal_1.pack()
    admin_verhaal_2.pack()
    admin_verhaal_3.pack()
    return root, menu


def verhaal_1(root, menu):
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: admin_scherm(root, menu))
    cancel_button.pack(padx=5, pady=5, side="right")

    frame = Frame(root, bg="#ded9ee")
    frame.pack(fill="both", expand=True)

    titel = Label(frame, text="Verhaal 1", font="Roboto, 24", bg="#ded9ee")
    ondertitel = Label(frame, text="Goede keuzes:", font="Roboto, 20", bg="#ded9ee")
    titel.pack(padx=25, pady=25)
    ondertitel.pack()
    verhaal_keuzes_frame = Frame(frame, height=400, width=500, bg="#ded9ee")
    verhaal_keuzes_frame.place(anchor="center", relx=0.5, rely=0.5)
    with open("files/avontuurgegevens.json") as bestand:
        inhoud = json.load(bestand)
        for onderdelen in inhoud['locaties']:
            if inhoud['locaties'][onderdelen]['einde'] == 'goed':
                for i in range(len(inhoud["locaties"][onderdelen]["keuzes"])):
                        keuzes = Label(verhaal_keuzes_frame,
                                   text=f'{i}. {inhoud["locaties"][onderdelen]["keuzes"][i]}', bg="#ded9ee",
                                       font="Roboto, 5")
                        keuzes.pack()
            else:
                pass


def verhaal_2(root, menu):
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: admin_scherm(root, menu))
    cancel_button.pack(padx=5, pady=5, side="right")
    titel = Label(root, text="Verhaal 2", font="Roboto, 24")
    ondertitel = Label(root, text="Goede keuzes:", font="Roboto, 20")
    titel.pack(padx=25, pady=25)
    ondertitel.pack()

    verhaal_keuzes_frame = Frame(root, height=400, width=500, bg="red")
    verhaal_keuzes_frame.place(anchor="center", relx=0.5, rely=0.5)
    with open("files/avontuurgegevens_2.json") as bestand:
        inhoud = json.load(bestand)
        for onderdelen in inhoud['locaties']:
            if inhoud['locaties'][onderdelen]['einde'] == "goed":
                for i in range(len(inhoud["locaties"][onderdelen]["keuzes"])):
                        keuzes = Label(verhaal_keuzes_frame,
                                   text=f'{i}. {inhoud["locaties"][onderdelen]["keuzes"][i]}')
                        keuzes.pack()
            else:
                pass
def verhaal_3(root, menu):
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: admin_scherm(root, menu))
    cancel_button.pack(padx=5, pady=5, side="right")
    titel = Label(root, text="Verhaal 3", font="Roboto, 24")
    ondertitel = Label(root, text="Goede keuzes:", font="Roboto, 20")
    titel.pack(padx=25, pady=25)
    ondertitel.pack()

    verhaal_keuzes_frame = Frame(root, height=400, width=500, bg="red")
    verhaal_keuzes_frame.place(anchor="center", relx=0.5, rely=0.5)

    with open("files/avontuurgegevens_3.json") as bestand:
        inhoud = json.load(bestand)
        for onderdelen in inhoud['locaties']:
            if inhoud['locaties'][onderdelen]['einde'] == "goed":
                for i in range(len(inhoud["locaties"][onderdelen]["keuzes"])):
                        keuzes = Label(verhaal_keuzes_frame,
                                   text=f'{i}. {inhoud["locaties"][onderdelen]["keuzes"][i]}')
                        keuzes.pack()
            else:
                pass