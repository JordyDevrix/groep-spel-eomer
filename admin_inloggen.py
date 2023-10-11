from tkinter import *

def admin_scherm(root,menu):
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")

    titel = Label(root, text="Admin login", font=("Roboto", 24))
    titel.pack(padx= 25, pady= 25)

    admin_login_frame = Frame(root, bg="grey")
    admin_login_frame.place(anchor="center", relx=0.5, rely=0.5)

    gebruikersnaam_label = Label(admin_login_frame, text="Gebruikersnaam")
    input_gebruikersnaam = Entry(admin_login_frame, bd=5)

    wachtwoord_label = Label(admin_login_frame, text="Wachtwoord")
    input_wachtwoord = Entry(admin_login_frame, bd=5, show="*")

    inlog_button = Button(admin_login_frame, width=25, height=2, text="Log in", command=lambda: print_tekst(input_gebruikersnaam, input_wachtwoord))


    gebruikersnaam_label.pack(padx=5, pady=5)
    input_gebruikersnaam.pack(padx=5, pady=5)
    wachtwoord_label.pack(padx=5, pady=5)
    input_wachtwoord.pack(padx=5, pady=5)
    inlog_button.pack(padx=5, pady=5)
    return root