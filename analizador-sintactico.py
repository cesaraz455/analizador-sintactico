from ast import Delete
import linecache
import os
import re
from tkinter import *
from tkinter import filedialog
import json
from turtle import clone


def GUI():    
    terminales = ["$", "interrogacion","plural","que","una","el","su","un","estar","encendido","a","yo","usted","tema","conexion","internet","bombillo","router","servicio","mantenimiento","no_pasado","colaborar","tener","desear","en","de"]
    simboloInicial = "O"

    def buscar_table():         #abre el .json con la informacion
        with open(ExamineRoute.cget("text"), encoding='utf-8-sig') as json_file:
            return json.load(json_file)    

    def browseFiles():                  
        rutfichero = filedialog.askopenfilename(initialdir = "/",title = "Select a File")
        ExamineRoute.configure(text=rutfichero) 

    def getRouteTAS():
        w = TokenText.get().split(" ")  # Obtiene: oracion
        return w

    def analizador():
        M = buscar_table()
        CmpResult.delete('1.0', END)

        w = getRouteTAS()
        n_w = getRouteTAS()  # Obtiene: oracion
        w.append("$") # w$
        n_w.append("$") # n_w$
        pila = ["$"]
        pila.append(simboloInicial)
        ae = w[0] # apunta ae al primer simbolo de w$
        X = ""
        n = len(w) # id + id * id $
        i = 0

        try:
            while X != "$" and i < n:
                X = pila[-1] # obtener el simbolo de la cima de la pila

                if(X in terminales or X == "$"):
                    if(X == ae):
                        pila.pop()
                        i = i + 1
                        if X != "$":
                            ae = w[i]
                            n_w.pop(0)
                            print(n_w)
                    else:
                        CmpResult.insert(INSERT, "Error de sintáxis. x001"  + "\n")
                        break
                else:
                    if M[X][ae] != "":
                        pila.pop()
                        if M[X][ae] != ["e"]:
                            for simbol in reversed(M[X][ae]):
                                pila.append(simbol)

                        CmpResult.insert(INSERT, X + "->" + "".join([str(elem) for elem in M[X][ae] ]) + "\t\t\t\t\t\t" + " ".join([str(elem) for elem in pila ]) + "\t\t\t\t\t\t" + " ".join([str(elem) for elem in n_w ]) + "\n")                    
                    else:
                        CmpResult.insert(INSERT, "Error de sintáxis. x002"  + "\n")
                        break
        except:
            CmpResult.insert(INSERT, "Error general de sintáxis"  + "\n")

    window = Tk()
    window.title('Analizador sintáctico | UCentral')
    window.geometry('1900x700')
    window['bg'] = "#F1F1F1"

    IntroLabel = Label(window,text="Bienvenido al programa para análisis de análisis sintáctico")
    IntroLabel.place(x=30,y=30)

    TASLabel = Label(window,text="Seleccione la tabla de análisis sintáctico")
    TASLabel.place(x=30,y=70)
    
    ExamineLabel = Button(window,text="Examinar",command=browseFiles)
    ExamineLabel.place(x=30,y= 95)

    ExamineRoute = Label(window, text="")
    ExamineRoute.place(x=100,y=95)

    TokenLabel = Label(window, text="Ingrese la cadena tokenizada")
    TokenLabel.place(x=30,y=130)

    TokenText = Entry(window, width=40)
    TokenText.place(x=30,y=160)

    CheckBtn = Button(window, text="Comprobar", command=analizador)
    CheckBtn.place(x=300,y=160)

    TokenLabel = Label(window, text="Salida:")
    TokenLabel.place(x=30,y=200)

    CmpResult = Text(window,width=230,height=25)
    CmpResult.place(x=30,y=230)

    window.mainloop()

if __name__ == '__main__':
    GUI()