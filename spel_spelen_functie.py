from tkinter import *

def verhaal_kiezen(root, menu):

    for widget in root.winfo_children():
        widget.destroy()



    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")


    cancel_button = Button(top_bar, width=3, height=1, text="X", command=lambda: menu(root))
    cancel_button.pack(padx=5, pady=5, side="right")

    avonturen_frame = Frame(root)
    avonturen_frame.place(anchor="center", relx=0.5, rely=0.5)

    avontuur_een = Button(root,width=50, height=30, bg='grey', text="Avontuur naar",command=lambda : verhaal_een(root))
    avontuur_een.place(anchor='center', relx=0.25, rely=0.5)



    # avontuur_een = Frame(avonturen_frame, width=400, height=700, bg="grey")
    # avontuur_een.grid(padx=20, pady=5, column=0, row=0)

    # avontuur_twee = Frame(avonturen_frame, width=400, height=700, bg="grey")
    # avontuur_twee.grid(padx=20, pady=5, column=1, row=0)
    #
    # avontuur_drie = Frame(avonturen_frame, width=400, height=700, bg="grey")
    # avontuur_drie.grid(padx=20, pady=5, column=2, row=0)
    #





    def verhaal_een(venster):
        from meerdere_keuzes import start_tekst_avontuur
        for widget in venster.winfo_children():
            widget.destroy()

        verhaal_een_button = Button(venster, text="Verhaal 1", font="Roboto, 24", command=start_tekst_avontuur(venster))
