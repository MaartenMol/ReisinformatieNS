#ReisinformatieNS main application
#Gemaakt door Bastiaan Ebbenhorst, Joshua Offermans, Maarten Mol, Thomas Mocellin
#Version 0.2

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
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']
        vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16] # 18:36
        trein = vertrek['TreinSoort']
        spoor = str(vertrek['VertrekSpoor'])
        spoor1 = spoor.replace("OrderedDict([('@wijziging', 'false'), ('#text', '", "")
        spoor2 = spoor1.replace("')])", "")
        spoor3 = spoor2.replace("OrderedDict([('@wijziging', 'true'), ('#text', '", "")
        gegevens += str('Om '+vertrektijd+' vertrekt er een ' + trein + ' richting '+ eindbestemming + ' van spoor ' + spoor3 + '\n')
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

    #Close InfoMenu
    def closeInfoMenu():
        app.deiconify()
        infoMenu.destroy()

    #Top border
    label = Label(master=infoMenu, text='', background='#ffcf1a')
    label.pack()

    #Bottom border
    label = Label(master=infoMenu, height=10, text='', background='#ffcf1a')
    label.pack(side=BOTTOM)

    #infoMenu Buttons and Input
    button3 = Button(master=infoMenu, font=('Frutiger', 16, 'bold'), foreground='white', background='#01236a', text='Reisinformatie ophalen', command=NotInUse)
    button3.place(x=495, y=465)
    entry1 = Entry(master=infoMenu, font=('Frutiger', 16, 'bold'), foreground='white', background='#01236a', width=20,)
    entry1.place(x=200, y=472)
    label = Label(master=infoMenu, font=('Frutiger', 16, 'bold'), foreground='white', text='Vanaf station:', background='#01236a')
    label.place(x=25, y=470)

    #Footer Image
    footerInfoMenuImagePath = "sources/footerInfoMenu.jpg"
    footerInfoMenuImage = ImageTk.PhotoImage(PIL.Image.open(footerInfoMenuImagePath))
    footerInfoMenuImagePanel = Label(infoMenu, image = footerInfoMenuImage, borderwidth= 0)
    footerInfoMenuImagePanel.place(x=0, y=553)

    #Stopbutton
    stopbutton = Button(master=infoMenu, font=('Frutiger', 10, 'bold'), foreground='white', background='red', text='Stoppen \n en naar beginscherm', command=closeInfoMenu)
    stopbutton.place(x=640, y=555)

    #Scrollbar
    scrollbar = Scrollbar(infoMenu)
    scrollbar.pack(side="right", fill=Y, expand=False)

    #Reisgegevens Output GUI
    gegevens = reisInfo(Station)
    text = Text(infoMenu, font=('Frutiger', 12, 'bold'), foreground='white', background='#01236a')
    text.insert(INSERT, gegevens)
    text.pack()
    scrollbar.config (command = text.yview)

#Not in use warning
def NotInUse():
    bericht = 'Deze functie is niet beschikbaar in onze App!'
    showinfo(title='Melding Reisinformatie NS', message=bericht)

#Beta warning
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

#Start main App
app.mainloop()
