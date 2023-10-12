from tkinter import *
from tkinter.ttk import Progressbar


def settings(root, menu, mixer):
    volume = 10
    for widget in root.winfo_children():
        widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    settings_menu_frame = Frame(root)
    settings_menu_frame.pack(fill="both", expand=True)

    settings_frame = Frame(settings_menu_frame, height=500, width=800, bg="grey")
    settings_frame.place(anchor="center", relx=0.5, rely=0.5)

    volume_setting_frame = Frame(settings_frame, bg="pink")
    volume_setting_frame.pack(padx=20, pady=10)

    volume_progress = Label(volume_setting_frame, text="leuke settings")
    volume_progress.grid(row=0, column=1)

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")


