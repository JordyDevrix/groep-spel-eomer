from tkinter import *
import json
#test
def check_inlog(input_gebruikersnaam, input_wachtwoord, root, menu):
    with open("admin_inlog.json") as bestand:
        inhoud = json.load(bestand)
    if input_gebruikersnaam == inhoud['gebruikersnaam'] and input_wachtwoord == inhoud['wachtwoord']:
        print("Ingelogd")
        admin_scherm(root, menu)
    elif input_gebruikersnaam == inhoud['gebruikersnaam'] and input_wachtwoord != inhoud['wachtwoord']:
        melding = Label()



def admin_inlogscherm(root, menu):
    for widget in root.winfo_children():
        widget.destroy()
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

    admin_verhaal1 = Button(verhaal_button_frame,
                          text="Verhaal 1",
                          font="Roboto, 20",
                          width=40,
                          command=lambda: verhaal_1(root, menu))
    admin_verhaal2 = Button(verhaal_button_frame,
                          text="Verhaal 2",
                          font="Roboto, 20",
                          width=40,
                          command=lambda: verhaal_2(root, menu))
    admin_verhaal3 = Button(verhaal_button_frame,
                          text="Verhaal 3",
                          font="Roboto, 20",
                          width=40,
                          command=lambda: verhaal_3(root, menu))
    admin_verhaal1.pack()
    admin_verhaal2.pack()
    admin_verhaal3.pack()
    return root, menu

def verhaal_1(root, menu):
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: admin_scherm(root, menu))
    cancel_button.pack(padx=5, pady=5, side="right")
    titel = Label(root, text="Verhaal 1", font="Roboto, 24")
    ondertitel = Label(root, text="Goede keuzes:", font="Roboto, 20")
    titel.pack(padx=25, pady=25)
    ondertitel.pack()

    verhaal_keuzes_frame = Frame(root, height=400, width=500, bg="red")
    verhaal_keuzes_frame.place(anchor="center", relx=0.5, rely=0.5)

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