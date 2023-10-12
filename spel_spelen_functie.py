from tkinter import *

def verhaal_kiezen(root, menu):

    for widget in root.winfo_children():
        widget.destroy()


    # button_tl = Button(root, text="Tijd/Locatie", command=lambda: tijd_locatie_weergeven(root))
    # button_tl.place(x=20, y=750)
    #
    # root.mainloop()
    # for widget in root.winfo_children():
    #     widget.destroy()

    top_bar = Frame(root, bg="grey", height=40)
    top_bar.pack(fill="both")

    avonturen_frame = Frame(root)
    avonturen_frame.place(anchor="center", relx=0.5, rely=0.5)

    avontuur_een = Button(root,width=50, height=30, bg='grey', text="Verhaal 1",command=lambda : verhaal_een(root))
    avontuur_een.place(anchor='center', relx=0.25, rely=0.5)



    # avontuur_een = Frame(avonturen_frame, width=400, height=700, bg="grey")
    # avontuur_een.grid(padx=20, pady=5, column=0, row=0)

    # avontuur_twee = Frame(avonturen_frame, width=400, height=700, bg="grey")
    # avontuur_twee.grid(padx=20, pady=5, column=1, row=0)
    #
    # avontuur_drie = Frame(avonturen_frame, width=400, height=700, bg="grey")
    # avontuur_drie.grid(padx=20, pady=5, column=2, row=0)
    #




    # cancel_button = Button(top_bar, width=3, height=
    # 1, text="X", command=lambda: menu(root))
    # cancel_button.pack(padx=5, pady=5, side="right")
    def verhaal_een(venster):
        for widget in venster.winfo_children():
            widget.destroy()

        test_label = Label(venster, text="Hallo")
        test_label.pack()
