#ReisinformatieNS main application
#Gemaakt door Bastiaan Ebbenhorst, Joshua Offermans, Maarten Mol, Thomas Mocellin
#Version 0.1

#Import
import requests
import xmltodict
from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter.messagebox import showinfo

#Main App Settings
def windowconfig(window):
    window.iconbitmap('sources/ns.ico')
    window.configure(background='#ffcf1a')
    window.geometry('{}x{}'.format(790,600))
    window.resizable(width=False, height=False)

#Main App Settings
app = Tk()
app.title("NS Kaartenautomaat")
windowconfig(app)

#Reis Info API
def reisInfo(Station):

    #API Authentication
    auth_details = ('joshuajessy47@gmail.com', 'vlgUm9-dkCiFX8swDoQ4uNdO1kiNtZhBs1CAIkbJl6gX3946BJ8uEQ')

    #API Query
    api_url = 'http://webservices.ns.nl/ns-api-avt?station='+ Station
    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)
    gegevens = ''


    #Result
    print('Dit zijn de vertrekkende treinen:')
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']
        vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16] # 18:36
        gegevens += str('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming + '\n')
    return gegevens

#Reis Info Menu
def reisInfoMenu():
    Station = 'Utrecht'
    global footerInfoMenuImage
    global infoMenu
    app.withdraw()
    infoMenu = Toplevel()
    infoMenu.title("Reisinformatie | NS Kaartenautomaat")
    windowconfig(infoMenu)

    #infoMenu Label
    label = Label(master=infoMenu, text='Reisinformatie NS BETA By Joshua & Maarten', background='red')
    label.pack()

    #infoMenu Buttons and Input
    button3 = Button(master=infoMenu, font=('Frutiger', 16, 'bold'), foreground='white', background='#01236a', text='Reisinformatie ophalen', command=NotInUse)
    button3.place(x=420, y=425)
    entry1 = Entry(master=infoMenu, font=('Frutiger', 16, 'bold'), foreground='white', background='#01236a', width=20,)
    entry1.place(x=120, y=430)

    #Footer Image
    footerInfoMenuImagePath = "sources/footerInfoMenu.jpg"
    footerInfoMenuImage = ImageTk.PhotoImage(PIL.Image.open(footerInfoMenuImagePath))
    footerInfoMenuImagePanel = Label(infoMenu, image = footerInfoMenuImage, borderwidth= 0)
    footerInfoMenuImagePanel.place(x=0, y=553)

    #Stopbutton
    stopbutton = Button(master=infoMenu, font=('Frutiger', 10, 'bold'), foreground='white', background='red', text='Stoppen \n en naar beginscherm', command=app.deiconify)
    stopbutton.place(x=640, y=555)

    #Reisgegevens Output GUI
    gegevens = reisInfo(Station)
    text = Text(infoMenu)
    text.insert(INSERT, gegevens)
    text.pack()

#Functions
def NotInUse():
    bericht = 'Deze functie is niet beschikbaar in onze App!'
    showinfo(title='Melding Reisinformatie NS', message=bericht)

#App Label
label = Label(master=app, text='Reisinformatie NS BETA By Joshua & Maarten', background='red')
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
button0 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='#01236a', text='Ik wil reizen naar', command=NotInUse)
button0.place(x=50, y=425)
button1 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='#01236a', text='Ik heb een OV-Chipkaart', command=NotInUse)
button1.place(x=275, y=425)
button2 = Button(master=app, font=('Frutiger', 16, 'bold'), foreground='white', background='#01236a', text='Reisinformatie', command=reisInfoMenu)
button2.place(x=575, y=425)

#Show main App
app.mainloop()
