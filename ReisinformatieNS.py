#ReisinformatieNS main application
#Gemaakt door Bastiaan Ebbenhorst, Joshua Offermans, Maarten Mol, Thomas Mocellin
#Version 0.1

#Import
from PIL import ImageTk
import PIL.Image
from  tkinter import *
from tkinter.messagebox import showinfo

#Main App Settings
app = Tk()
app.configure(background='#fcc917')
app.title("Reisinformatie NS V0.1")
app.geometry('{}x{}'.format(790,600))
app.resizable(width=False, height=False)

#Functions
def NotInUse():
	bericht = 'Deze functie is niet beschikbaar in onze App!'
	showinfo(title='Melding Reisinformatie NS', message=bericht)

#App Label
#label = Label(master=app, text='Reisinformatie NS V0.1', background='yellow')
#label.pack()

#Footer Image
path = "balk.jpg"
img = ImageTk.PhotoImage(PIL.Image.open(path))
panel = Label(app, image = img)
panel.place(x=0, y=549)

#App Buttons
button0 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='blue', text='Ik wil reizen naar', command=NotInUse)
button0.place(x=100, y=400)
button1 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='blue', text='Ik heb een OV-Chipkaart', command=NotInUse)
button1.place(x=300, y=400)
button2 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='blue', text='Reisinformatie')
button2.place(x=600, y=400)

#Show main App
app.mainloop()
