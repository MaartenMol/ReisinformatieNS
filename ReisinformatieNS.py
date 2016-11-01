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
app.configure(background='#fece22')
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

#main img
path1 = "beginscherm.jpg"
img1 = ImageTk.PhotoImage(PIL.Image.open(path1))
panel1 = Label(app, image = img1, borderwidth= 0)
panel1.place(x=0, y=25)

#Footer Image
path2 = "balk.jpg"
img2 = ImageTk.PhotoImage(PIL.Image.open(path2))
panel2 = Label(app, image = img2, borderwidth= 0)
panel2.place(x=0, y=555)

#App Buttons
button0 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='#003399', text='Ik wil reizen naar', command=NotInUse)
button0.place(x=100, y=400)
button1 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='#003399', text='Ik heb een OV-Chipkaart', command=NotInUse)
button1.place(x=300, y=400)
button2 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='#003399', text='Reisinformatie')
button2.place(x=600, y=400)

#Show main App
app.mainloop()
