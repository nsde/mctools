from tkinter import *
# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Test')
tkFenster.geometry('120x125')
# Rahmen Radiobutton
frameRadiobutton = Frame(master=tkFenster, bg='#FFCFC9')
frameRadiobutton.place(x=5, y=5, width=110, height=80)
# Rahmen Ausgabe
frameAusgabe = Frame(master=tkFenster, bg='#D5E88F')
frameAusgabe.place(x=5, y=90, width=110, height=30)
# Kontrollvariable
tageszeit = StringVar()
# Radiobutton
radiobutton1 = Radiobutton(master=frameRadiobutton, anchor='w',
                           text='morgens', value='Guten Morgen!', variable=tageszeit)
radiobutton1.place(x=5, y=5, width=100, height=20)
radiobutton2 = Radiobutton(master=frameRadiobutton, anchor='w',
                           text='mittags', value='Guten Tag!', variable=tageszeit)
radiobutton2.place(x=5, y=30, width=100, height=20)
radiobutton3 = Radiobutton(master=frameRadiobutton, anchor='w',
                           text='abends', value='Guten Abend!', variable=tageszeit)
radiobutton3.place(x=5, y=55, width=100, height=20)
radiobutton1.select()
# Label Text
labelText = Label(master=frameAusgabe, bg='white', textvariable=f"tageszeit")
labelText.place(x=5, y=5, width=100, height=20)
# Aktivierung des Fensters
tkFenster.mainloop()