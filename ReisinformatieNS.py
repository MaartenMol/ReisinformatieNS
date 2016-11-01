#ReisinformatieNS main application
#Gemaakt door Bastiaan Ebbenhorst, Joshua Offermans, Maarten Mol, Thomas Mocellin
#Version 0.1

#Import
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter.messagebox import showinfo

#Main App Settings
def windowset(app):
    app.iconbitmap('sources/ns.ico')
    app.configure(background='#fece22')
    app.geometry('{}x{}'.format(790,600))
    app.resizable(width=False, height=False)
app = Tk()
app.title("NS Kaartenautomaat")
windowset(app)
#Reis Info Menu
def reisInfoMenu():
    infoMenu = Tk()
    app.withdraw()
    windowset(infoMenu)
    #infoMenu Label
    label = Label(master=infoMenu, text='Reisinformatie NS BETA By Joshua & Maarten', background='yellow')
    label.pack()

    #infoMenu Buttons and Input
    button3 = Button(master=infoMenu, font=('Frutiger', 16, 'bold'), foreground='white', background='#003399', text='Reisinformatie ophalen', command=NotInUse)
    button3.place(x=420, y=425)
    entry1 = Entry(master=infoMenu, font=('Frutiger', 16, 'bold'), foreground='white', background='#003399', width=20,)
    entry1.place(x=120, y=430)

    #Footer Image
    footerInfoMenuImagePath = "sources/footerInfoMenu.jpg"
    footerInfoMenuImage = ImageTk.PhotoImage(PIL.Image.open(footerInfoMenuImagePath))
    footerInfoMenuImagePanel = Label(infoMenu, image = footerInfoMenuImage, borderwidth= 0)
    footerInfoMenuImagePanel.place(x=0, y=555)

#Functions
def NotInUse():
    bericht = 'Deze functie is niet beschikbaar in onze App!'
    showinfo(title='Melding Reisinformatie NS', message=bericht)

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
button2 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='#003399', text='Reisinformatie', command=reisInfoMenu)
button2.place(x=575, y=425)

#Show main App
app.mainloop()
