from tkinter import *
from admin_inloggen import *
from character_maken import character_maken
from pygame import mixer
import pygame.constants
from PIL import Image, ImageTk
from _thread import start_new_thread
import threading


def music():
    mixer.init()
    mixer.music.load("music/lordapp vol1 preview2.mp3")
    mixer.music.play(-1)
    mixer.music.set_endevent(pygame.constants.USEREVENT)


def introsound():
    mixer.init()
    mixer.music.load("music/introsound.mp3")
    mixer.Channel(1).play(pygame.mixer.Sound('music/introsound.mp3'))
    mixer.music.set_endevent(pygame.constants.USEREVENT)


def settings(root):
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    char = Frame(root)
    char.pack()
    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")


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

    # speel_spel = Button(menu_button_frame, text="PLAY GAME", font="Roboto, 20", width=40, command=lambda: spel_spelen(root))
    # speel_spel.pack(padx=10, pady=10, fill="both")

    settings_optie = Button(menu_button_frame,
                            text="SETTINGS",
                            font="Roboto, 20",
                            width=40,
                            command=lambda: settings(root))
    settings_optie.pack(padx=10, pady=10, fill="both")

    admin_opties = Button(menu_button_frame,
                          text="ADMIN MODE",
                          font="Roboto, 20",
                          width=40,
                          command=lambda: admin_inlogscherm(root, menu))
    admin_opties.pack(padx=10, pady=10, fill="both")

    root.mainloop()


def applicatie_gui():

    root = Tk()
    root.geometry("1400x800")
    root.resizable(False, False)
    app_frame = Frame(root)
    app_frame.pack(fill="both", expand=True)

    # bouw splashscreen code
    splash_screen = Frame(root)
    splash_screen.pack()
    logo_image = PhotoImage(file= "images/lord_of_the_rings_logo.png")
    logo_label = Label(root, image= logo_image)
    logo_label.place(anchor="center", relx=0.5, rely=0.5)
    root.after(5000, menu, root)

    threading.Thread(target=music).start()

    root.mainloop()
