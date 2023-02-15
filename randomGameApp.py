from tkinter import *
from tkinter import ttk    
from tkinter import messagebox
from random import sample
from connection import *
from gameApp import *
import random

db = DataBase()

def buscarPregunta(lista):
    pass

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
        # inputPregunta.config(text=pregunta)

        messagebox.showinfo(title="Informacion",message="Acertaste")

    else:
        # ocultarWidget(pregunta)
        # ocultarWidget(button1)
        # ocultarWidget(button2)
        # ocultarWidget(button3)
        # ocultarWidget(button4)
        messagebox.showerror(title="Informacion",message=f"Erraste, la opcion correcta era la opcion {resultado}")

def generarNumeroAleatorio():
    numerosAleatorios = random.sample(range(3,60),10)
    return numerosAleatorios

#-------------------------------------------
numerosAleatorios = generarNumeroAleatorio()
print(numerosAleatorios)


def buscarPreguntaAleatoria():
    numerosAleatorios = generarNumeroAleatorio()
    for numero in numerosAleatorios:
        db.cursor.execute(f"SELECT * FROM preguntados WHERE id = {numero}")
        rows = db.cursor.fetchall()
        preguntas = []
        for row in rows:
            print(row)
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
        


mainWindow = Tk()
mainWindow.title("Juego de preguntas y respuestas")
mainWindow.config(width=800,height=600)
mainWindow.resizable(0,0)

#Input
inputPregunta = Label(mainWindow,text="Clickee en iniciar para obtener 10 preguntas al azar:")
inputPregunta.place(x=50,y=50)

btnBuscar = Button(mainWindow,text="Iniciar", command=buscarPreguntaAleatoria)
btnBuscar.config(width=6)
btnBuscar.place(x=80,y=75)

btnVolver = Button(mainWindow,text="Volver")
btnVolver.config(width=10)
btnVolver.place(x=150,y=75)


mainWindow.mainloop()