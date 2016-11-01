#ReisinformatieNS main application
#Gemaakt door Bastiaan Ebbenhorst, Joshua Offermans, Maarten Mol, Thomas Mocellin
#Version 0.1

#Import
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter.messagebox import showinfo



#Main App Settings
app = Tk()
app.iconbitmap('sources/ns.ico')
app.configure(background='#fece22')
app.title("Reisinformatie NS V0.1")
app.geometry('{}x{}'.format(790,600))
app.resizable(width=False, height=False)

#Reis Info Menu Settings
#info = Tk()
#info.iconbitmap('sources/ns.ico')
#info.configure(background='#fece22')
#info.title("Reisinformatie NS V0.1")
#info.geometry('{}x{}'.format(790,600))
#info.resizable(width=False, height=False)

def quit():
    app.destroy()

#window2
def win2():
        app.withdraw()
        new = Toplevel()
        new.title('Window 2')
        mainframe = Frame(new, padding = '3 3 12 12')
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)

        Button(mainframe, text = 'Next', command = win2).grid(
            column = 1, row = 1, sticky = W)

#Functions
def NotInUse():
	bericht = 'Deze functie is niet beschikbaar in onze App!'
	showinfo(title='Melding Reisinformatie NS', message=bericht)

def ReisInfoMenu():
	app.mainloop()

#App Label
label = Label(master=app, text='Reisinformatie NS BETA By Joshua & Maarten', background='yellow')
label.pack()

#Main Image
mainImagePath = "sources/main.jpg"
mainImage = ImageTk.PhotoImage(PIL.Image.open(mainImagePath))
mainImagePanel = Label(app, image = mainImage, borderwidth= 0)
mainImagePanel.place(x=115, y=100)

#Footer Image
footerImagePath = "sources/footer.jpg"
footerImage = ImageTk.PhotoImage(PIL.Image.open(footerImagePath))
footerImagePanel = Label(app, image = footerImage, borderwidth= 0)
footerImagePanel.place(x=0, y=555)

#App Buttons
button0 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='#003399', text='Ik wil reizen naar', command=NotInUse)
button0.place(x=50, y=425)
button1 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='#003399', text='Ik heb een OV-Chipkaart', command=NotInUse)
button1.place(x=275, y=425)
button2 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='#003399', text='Reisinformatie', command=win2)
button2.place(x=575, y=425)





#Show main App
app.mainloop()
