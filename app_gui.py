from tkinter import *
from admin_inloggen import *
from character_maken import character_maken
from PIL import Image, ImageTk
import threading
from settings_menu import settings
from game_muziek import music


def kill_process(root, menu_return):
    settings_menu_frame = Frame(root, width=500, height=300, bg="grey")
    settings_menu_frame.place(anchor="center", relx=0.5, rely=0.5)
    quit_text = Label(settings_menu_frame, text="Are you sure you want to quit?", font="Roboto, 16", bg="grey")
    quit_text.pack(pady=10, padx=10)

    def quit_game():
        print("ending game")
        root.destroy()

    quitter_frame = Frame(settings_menu_frame, bg="grey")
    quitter_frame.pack()

    quit_button = Button(quitter_frame,
                         text="yes",
                         width=10,
                         height=3,
                         bg="red",
                         command=quit_game)
    quit_button.pack(side="left", padx=10, pady=10)

    cancel_button = Button(quitter_frame,
                           text="no",
                           width=10,
                           height=3,
                           bg="green",
                           command=lambda: menu_return(root))
    cancel_button.pack(side="right", padx=10, pady=10)


# def tijd_locatie_weergeven(root):
#     for widget in root.winfo_children():
#         widget.destroy()
#
#     tijd = "10:12"
#     locatie = "Rivendel"
#
#     frame1 = Frame(root, width=300, height=120, highlightbackground="blue", highlightthickness=6)
#     frame1.place(x=600, y=340)
#
#     lt_label = Label(frame1, text=f"{tijd} en {locatie}", font=("Roboto", 24))
#     lt_label.grid(row=0, column=0, pady=20)
#
#     close_button = Button(frame1, text="x", command=lambda: spel_spelen(root))
#     close_button.grid(row=1, column=0)


def menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    bg_image = PhotoImage(file="images/Character_kies_achtegrond-transformed (1).png")

    bg_label = Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    menu_button_frame = Frame(height=200, width=400, bg="Green")
    menu_button_frame.place(anchor="center", relx=0.5, rely=0.5)

    maak_character = Button(menu_button_frame,
                            text="CREATE A CHARACTER",
                            font="Roboto, 20",
                            width=40,
                            command=lambda: character_maken(root, menu))
    maak_character.pack(padx=10, pady=10, fill="both")

    settings_menu = Button(menu_button_frame,
                           text="SETTINGS",
                           font="Roboto, 20",
                           width=40,
                           command=lambda: settings(root, menu))
    settings_menu.pack(padx=10, pady=10, fill="both")

    # speel_spel = Button(menu_button_frame, text="PLAY GAME", font="Roboto, 20", width=40, command=lambda: spel_spelen(root))
    # speel_spel.pack(padx=10, pady=10, fill="both")

    admin_opties = Button(menu_button_frame,
                          text="ADMIN MODE",
                          font="Roboto, 20",
                          width=40,
                          command=lambda: admin_inlogscherm(root, menu))
    admin_opties.pack(padx=10, pady=10, fill="both")

    quit_button = Button(menu_button_frame,
                         text="QUIT GAME",
                         font="Roboto, 20",
                         width=40,
                         command=lambda: kill_process(root, menu))
    quit_button.pack(padx=10, pady=10, fill="both")

    root.mainloop()


def applicatie_gui():
    root = Tk()
    root.geometry("1400x800")
    root.iconbitmap("images/lord_of_the_rings_icon.ico")
    root.title("Lord of The Rings")

    root.resizable(False, False)
    app_frame = Frame(root, bg="black")
    app_frame.pack(fill="both", expand=True)

    # bouw splashscreen code
    splash_screen = Frame(root, bg="black")
    splash_screen.pack()
    logo_image = PhotoImage(file= "images/lord_of_the_rings_logo.png")
    logo_label = Label(root, image= logo_image, bg="black")
    logo_label.place(anchor="center", relx=0.5, rely=0.5)
    root.after(5000, menu, root)

    threading.Thread(target=music).start()

    root.mainloop()
