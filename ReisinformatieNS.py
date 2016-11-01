#ReisinformatieNS main application
#Gemaakt door Bastiaan Ebbenhorst, Joshua Offermans, Maarten Mol, Thomas Mocellin
#Version 0.1

from tkinter import *
top = Tk()

#App Label
label = Label(master=top, text='Reisinformatie NS V0.1', background='yellow')
label.pack()

#App Buttons
button = Button(master=top, font=('Frutiger', 16, 'bold'), foreground='white', background='blue', text='Reisinformatie')
button.pack(pady=10)


top.configure(background='#fcc917')
top.geometry('{}x{}'.format(900,600))
top.mainloop()
