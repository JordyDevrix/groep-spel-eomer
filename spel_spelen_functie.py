from tkinter import *

def verhaal_kiezen(root, menu):

    for widget in root.winfo_children():
        widget.destroy()



    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")


    frame = Frame(root)

    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")

    avonturen_frame = Frame(root)
    avonturen_frame.place(anchor="center", relx=0.5, rely=0.5)

    avontuur_een = Button(root,width=50, height=30, bg='grey', text="Avontuur naar",command=lambda : verhaal_een(root))
    avontuur_een.place(anchor='center', relx=0.25, rely=0.5)

    avontuur_twee = Button(root, width=50, height=30, command=lambda: verhaal_een(root))
    avontuur_twee.place(anchor='center', relx=0.50, rely=0.5)

    avontuur_drie = Button(root, width=50, height=30, command=lambda: verhaal_een(root))
    avontuur_drie.place(anchor='center', relx=0.75, rely=0.5)






    def verhaal_een(venster):
        from meerdere_keuzes import start_tekst_avontuur
        for widget in venster.winfo_children():
            widget.destroy()

        verhaal_een_button = Button(venster, text="Verhaal 1", font="Roboto, 24", command=start_tekst_avontuur(venster))
