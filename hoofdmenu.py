from tkinter import *

def hoofdmenu():
    root = Tk()
    root.geometry("1000x562")
    root.title("Hoofdmenu")
    root.configure(highlightbackground='black')

    bg = PhotoImage(file="images/LOTRBG.png")
    canvasBG = Canvas(root, width=1000,
                      height=562)
    canvasBG.pack(fill = "both", expand = True)
    canvasBG.create_image(0, 0, image = bg,
                          anchor = "nw")
    canvasBG.create_text(500, 50, text= "Welkom bij Lord of The Rings Legends", font=("Arial", 28))


    speel_button = Button(root, text="Speel",
                    font=("Arial", 24),
                    command=lambda : scherm_speel(root))


    kies_karakter_button = Button(root, text="Kies karakter",
                                  font=("Arial", 24),
                                  command= lambda : scherm_speel(root))

    afsluiten_button = Button(root, text="Afsluiten",
                                  font=("Arial", 24),
                                  command=lambda: quit())

    speel_button = canvasBG.create_window( 450, 125,
                                       anchor = "nw",
                                       window = speel_button)

    kies_karakter_button = canvasBG.create_window( 400, 200,
                                       anchor = "nw",
                                       window = kies_karakter_button)

    afsluiten_button = canvasBG.create_window( 430, 275,
                                       anchor = "nw",
                                       window = afsluiten_button)

    root.mainloop()


def scherm_speel(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = Label(root, text="Hallo")
    label.grid(column = 0, row = 0)

    labl = Label(root, text="Hallo")
    labl.grid(column=1, row=1)

def scherm_kies_karakter(root):
    for widget in root.winfo_children():
        widget.destroy()

        label = Label(root, text="Hallo")
        label.grid(column=0, row=0)

        labl = Label(root, text="Hallo")
        labl.grid(column=1, row=1)
#

#
    root.mainloop()