from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from connection import *

def mainGame(window):

    #creacion de objetto de la clase database
    db = DataBase()

    def volverAtras(window,mainWindow):
        window.deiconify()
        mainWindow.destroy()

    def ocultarWidget(widget):
        widget.place_forget()

    def comprobacionResultado(resultado,opciones,opcion,button1,button2,button3,button4,pregunta):
        #busca la posicion de la opcion elegida y la compara con el resultado que se le resta 1.,
        posicion = opciones.index(opcion)
        if  posicion == (resultado - 1):
            # ocultarWidget(pregunta)
            # ocultarWidget(button1)
            # ocultarWidget(button2)
            # ocultarWidget(button3)
            # ocultarWidget(button4)

            messagebox.showinfo(title="Informacion",message="Acertaste")
        else:
            # ocultarWidget(pregunta)
            # ocultarWidget(button1)
            # ocultarWidget(button2)
            # ocultarWidget(button3)
            # ocultarWidget(button4)
            messagebox.showerror(title="Informacion",message=f"Erraste, la opcion correcta era la opcion {resultado}")
        
    def buscarPregunta():
        entry = entryPregunta.get()
        db.cursor.execute(f"SELECT * FROM preguntados WHERE id = {entry}")
        rows = db.cursor.fetchall()
        preguntas = []
        for row in rows:
            idOpcion,pregunta,opcion1,opcion2,opcion3,opcion4,resultado = row

        opciones = [opcion1,opcion2,opcion3,opcion4]

        inputPreg = Label(mainWindow,text=pregunta,font=("Impact",20,"bold"))
        inputPreg.place(x=60,y=150)

        buttonOpcion1 = Button(mainWindow,text=opcion1,width=50, command=lambda:comprobacionResultado
        (resultado,opciones,opcion1,buttonOpcion1,buttonOpcion2,buttonOpcion3,buttonOpcion4,inputPreg))
        buttonOpcion1.place(x=60,y=200)

        buttonOpcion2 = Button(mainWindow,text=opcion2,width=50, command=lambda:comprobacionResultado(resultado,opciones,opcion2,buttonOpcion1,buttonOpcion2,buttonOpcion3,buttonOpcion4,inputPreg))
        buttonOpcion2.place(x=60,y=240)

        buttonOpcion3 = Button(mainWindow,text=opcion3,width=50, command=lambda:comprobacionResultado(resultado,opciones,opcion3,buttonOpcion1,buttonOpcion2,buttonOpcion3,buttonOpcion4,inputPreg))
        buttonOpcion3.place(x=60,y=280)

        buttonOpcion4 = Button(mainWindow,text=opcion4,width=50, command=lambda:comprobacionResultado(resultado,opciones,opcion4,buttonOpcion1,buttonOpcion2,buttonOpcion3,buttonOpcion4,inputPreg))
        buttonOpcion4.place(x=60,y=320)

    mainWindow = Toplevel()
    mainWindow.title("Juego de preguntas y respuestas")
    mainWindow.config(width=800,height=600)
    mainWindow.resizable(0,0)

    #Input
    inputPregunta = Label(mainWindow,text="Ingrese un numero de pregunta(1-60):")
    inputPregunta.place(x=50,y=50)

    entryPregunta = Entry(mainWindow)
    entryPregunta.config(width=25)
    entryPregunta.place(x=70,y=80)

    btnBuscar = Button(mainWindow,text="Buscar",command=buscarPregunta)
    btnBuscar.config(width=6)
    btnBuscar.place(x=230,y=75)

    btnVolver = Button(mainWindow,text="Volver",command=lambda:volverAtras(window,mainWindow))
    btnVolver.config(width=10)
    btnVolver.place(x=300,y=75)

    window.withdraw()
