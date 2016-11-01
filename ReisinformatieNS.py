#ReisinformatieNS main application
#Gemaakt door Bastiaan Ebbenhorst, Joshua Offermans, Maarten Mol, Thomas Mocellin
#Version 0.1

#Import
from tkinter import *
from tkinter.messagebox import showinfo

#Main App
top = Tk()

#Def
def NotInUse():
	bericht = 'Deze functie is niet beschikbaar in onze App!'
	showinfo(title='Melding Reisinformatie NS', message=bericht)

#App Label
label = Label(master=top, text='Reisinformatie NS V0.1', background='yellow')
label.pack()

#App Buttons
button0 = Button(master=top, font=('Frutiger', 16, 'bold'), foreground='white', background='blue', text='Ik wil reizen naar', command=NotInUse)
button0.place(x=100, y=400)
button1 = Button(master=top, font=('Frutiger', 16, 'bold'), foreground='white', background='blue', text='Ik heb een OV-Chipkaart', command=NotInUse)
button1.place(x=300, y=400)
button2 = Button(master=top, font=('Frutiger', 16, 'bold'), foreground='white', background='blue', text='Reisinformatie')
button2.place(x=600, y=400)



top.configure(background='#fcc917')
top.geometry('{}x{}'.format(900,600))
top.mainloop()
