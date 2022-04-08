from tkinter import *
from tkinter import filedialog

def GUI():

    noTerminales = ["E", "E'", "T", "T'", "F"]
    terminales = ["+", "*", "(", ")", "e", "id"]
    simboloInicial = "E"
    pila = ["$"]
    pila.append(simboloInicial)
    M = {
        "E": {
            "id": ["T", "E'"],
            "+": "",
            "*": "",
            "(": ["T", "E'"],
            ")": "",
            "$": ""
        },
        "E'": {
            "id": "",
            "+": ["+", "T", "E'"],
            "*": "",
            "(": "",
            ")": ["e"],
            "$": ["e"]
        },
        "T": {
            "id": ["F", "T'"],
            "+": "",
            "*": "",
            "(": ["F", "T'"],
            ")": "",
            "$": ""
        },
        "T'": {
            "id": "",
            "+": ["e"],
            "*": ["*", "F", "T'"],
            "(": "",
            ")": ["e"],
            "$": ["e"]
        },
        "F": {
            "id": ["id"],
            "+": "",
            "*": "",
            "(": ["(", "E", ")"],
            ")": "",
            "$": ""
        }
    }

    def browseFiles(): 
        fileRoute = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) 
        ExamineRoute.configure(text=fileRoute) 

    def analizador():
        CmpResult.delete('1.0', END)

        w = TokenText.get().split(" ")  # Obtiene: "id + id * id"
        w.append("$") # w$

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
                    else:
                        CmpResult.insert(INSERT, "Error de sintáxis. x001"  + "\n")
                        break
                else:
                    if M[X][ae] != "":
                        pila.pop()
                        if M[X][ae] != ["e"]:
                            for simbol in reversed(M[X][ae]):
                                pila.append(simbol)

                        CmpResult.insert(INSERT, X + "->" + "".join([str(elem) for elem in M[X][ae]])  + "\n")
                    else:
                        CmpResult.insert(INSERT, "Error de sintáxis. x002"  + "\n")
                        break
        except:
            CmpResult.insert(INSERT, "Error general de sintáxis"  + "\n")

    window = Tk()
    window.title('Analizador sintáctico | UCentral')
    window.geometry('400x500')
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

    CmpResult = Text(window,width=30,height=12)
    CmpResult.place(x=30,y=230)

    window.mainloop()

if __name__ == '__main__':
    GUI()