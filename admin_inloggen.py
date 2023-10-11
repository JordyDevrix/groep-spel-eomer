from tkinter import *
import json

def check_inlog(input_gebruikersnaam, input_wachtwoord, root, menu):
    with open("admin_inlog.json") as bestand:
        inhoud = json.load(bestand)
    if input_gebruikersnaam == inhoud['gebruikersnaam'] and input_wachtwoord == inhoud['wachtwoord']:
        print("Ingelogd")
        admin_scherm(root, menu)
    else:
        print("Inloggen mislukt")



def admin_inlogscherm(root, menu):
    for widget in root.winfo_children():
        widget.destroy()
    print(root)
    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command= lambda : menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")

    titel = Label(root, text="Admin login", font=("Roboto", 24))
    titel.pack(padx= 25, pady= 25)

    admin_login_frame = Frame(root, bg="grey")
    admin_login_frame.place(anchor="center", relx=0.5, rely=0.5)

    gebruikersnaam_label = Label(admin_login_frame, text="Gebruikersnaam")
    input_gebruikersnaam = Entry(admin_login_frame, bd=5)

    wachtwoord_label = Label(admin_login_frame, text="Wachtwoord")
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
    titel = Label(root, text="Admin portaal", font=("Roboto", 24))
    titel.pack(padx=25, pady=25)

    verhaal_button_frame = Frame(root, height=650, width=500, bg="red")
    verhaal_button_frame.place(anchor="center", relx=0.5, rely=0.5)

    admin_opties = Button(verhaal_button_frame,
                          text="Verhaal1",
                          font="Roboto, 20",
                          width=40)
    admin_opties.pack()
    return root, menu