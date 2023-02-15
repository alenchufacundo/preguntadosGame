from tkinter import *
from tkinter import ttk,messagebox ,simpledialog
from connection import *


def editWindow(window):

    #creacion de objetto de la clase database
    db = DataBase()

    def volverAtras(window,mainWindow):
        window.deiconify()
        mainWindow.destroy()

    def actualizar ():
        db.cursor.execute("SELECT * FROM preguntados")
        filas = db.cursor.fetchall()
        preguntas = []
        for fila in filas:
            idOpcion,pregunta,opcion1,opcion2,opcion3,opcion4,resultado = fila
            preguntas.append(pregunta)
        listaPreguntas.config(values=preguntas)
        messagebox.showinfo(title="Informacion",message="Preguntas actualizadas")


    def deletePregunta ():
        respuesta = messagebox.askyesno(title="Advertencia",message="Estas seguro de eliminar la pregunta?")
        if (respuesta):
            db.cursor.execute("SELECT * FROM preguntados")
            pregunta = listaPreguntas.get()
            filas = db.cursor.fetchall()
            for fila in filas:
                if pregunta in fila:
                    id = fila[0]       
            sql = f"DELETE FROM preguntados WHERE id = {id}"
            db.cursor.execute(sql)
            # db.connect.commit()
            listaPreguntas.set("")
            listaPreguntas.config(values="")
            messagebox.showinfo(title="Informacion",message="Pregunta eliminada, por favor, clickea en actualizar")

    def createPreguntas():
        pregunta = simpledialog.askstring(title="Ingreso",prompt="Inserte su pregunta", parent= editWindow)
        opcion1= simpledialog.askstring(title="Ingreso",prompt="Inserte una opcion", parent= editWindow)
        opcion2 = simpledialog.askstring(title="Ingreso",prompt="Inserte una opcion", parent= editWindow)
        opcion3 = simpledialog.askstring(title="Ingreso",prompt="Inserte una opcion", parent= editWindow)
        opcion4 = simpledialog.askstring(title="Ingreso",prompt="Inserte una opcion", parent= editWindow)
        respuesta = simpledialog.askstring(title="Ingreso",prompt="Inserte el numero de posicion donde se encuentra la opcion correcta", parent= editWindow)

        sql = f"INSERT INTO preguntados(pregunta,opcion1,opcion2,opcion3,opcion4,respuesta) VALUES ('{pregunta}','{opcion1}','{opcion2}','{opcion3}','{opcion4}','{respuesta}')"
        print(sql)
        db.cursor.execute(sql)
        # db.cursor.commit()
        messagebox.showinfo(title="Informacion",message="Pregunta agregada a la base de datos")


    editWindow = Toplevel()
    # editWindow = Tk()
    editWindow.title("Editor de preguntas y respuestas")
    editWindow.config(width=800,height=600)

    # labelTitle = Label(editWindow,text="Proximamente podras agregar, editar y eliminar preguntas/respuestas") 
    # labelTitle.place(x=100,y=50)
    labelTitle = Label(editWindow,text="Editor de preguntas y respuestas",font=("Arial",15,"bold"))
    labelTitle.place(x=50,y=50)

    listaPreguntas = ttk.Combobox(editWindow, width="70", height="40",state="readonly")
    listaPreguntas.place(x=50,y=100)

    buttonUpdate = Button(editWindow,text="Actualizar",command=actualizar)
    buttonUpdate.place(x=520,y=95)
    buttonDelete = Button(editWindow,text="Borrar", command=deletePregunta)
    buttonDelete.place(x=600,y=95)
    buttonCreate = Button(editWindow,text="Crear", command=createPreguntas)
    buttonCreate.place(x=660,y=95)
    btnVolver = Button(editWindow,text="Volver",command=lambda:volverAtras(window,editWindow))
    btnVolver.config(width=10)
    btnVolver.place(x=660,y=200)

    window.withdraw()

    # editWindow.mainloop()