
from admin_inloggen import *
from character_maken import character_maken
import threading
from settings_menu import settings
from game_muziek import music, introsound


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


def menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    bg_image = PhotoImage(file="images/Character_kies_achtegrond-transformed (1).png")

    # ================================ # maakt achtergrond resizable
    bg_image = bg_image.zoom(10)
    bg_image = bg_image.subsample(7)
    # ================================ #

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


def enter_game(root):
    for widget in root.winfo_children():
        widget.destroy()

    threading.Thread(target=music).start()

    label = Frame(root, bg="black")
    label.pack(fill="both", expand=True)

    root.after(1000, menu, root)


def applicatie_gui():
    root = Tk()
    root.geometry("1400x800")
    root.iconbitmap("images/lord_of_the_rings_icon.ico")
    root.title("Lord of The Rings")

    root.resizable(True, True)
    app_frame = Frame(root, bg="black")
    app_frame.pack(fill="both", expand=True)

    # bouw splashscreen code
    splash_screen = Frame(root, bg="black")
    splash_screen.pack()
    logo_image = PhotoImage(file= "images/lord_of_the_rings_logo.png")
    logo_label = Label(root, image= logo_image, bg="black")
    logo_label.place(anchor="center", relx=0.5, rely=0.5)
    root.after(3000, enter_game, root)

    threading.Thread(target=introsound).start()

    root.mainloop()
