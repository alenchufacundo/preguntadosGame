from tkinter import *
from gameApp import *

def preGameWindow(window):

    def volverAtras(window,mainWindow):
        window.deiconify()
        mainWindow.destroy()

    # preGameWindow = Tk ()
    preGameWindow = Toplevel ()
    preGameWindow.title("Main game")
    preGameWindow.config(width=600,height=400)

    buttonJuegoPersonalizado = Button(preGameWindow,text="Juego Facil",width=20,command=lambda:mainGame(preGameWindow))
    buttonJuegoPersonalizado.place(x=200,y=100)

    buttonJuegoAleatorio = Button(preGameWindow,text="Juego Dificil",width=20)
    buttonJuegoAleatorio.place(x=200,y=150)

    btnVolver = Button(preGameWindow, text="Volver",width=15,command=lambda:volverAtras(window,preGameWindow))
    btnVolver.place(x=300,y=300)

    # preGameWindow.mainloop()