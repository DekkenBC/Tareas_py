import tkinter as tk
from tkinter import messagebox
import math

Calculadora = tk.Tk()
Calculadora.title("Calculadora")
Calculadora.geometry("570x550")
Calculadora.iconbitmap("Python_TK/Calculator.ico")
Calculadora.resizable(False,False)
Calculadora.configure(background="gray30")

Memory = "0"
Ecuacion = ""
Simbolo = False
resultado = ""

def Escribir(Value):
    global Ecuacion, Simbolo
    if Value == "*" or Value == "/" or Value == "+" or Value == "-":
        if Simbolo:
            Ecuacion = Ecuacion[:-1]
            Ecuacion = Ecuacion + Value
            label_resultado.config(text = Ecuacion)
        else:
            Simbolo = True
            Ecuacion = Ecuacion + Value
            label_resultado.config(text = Ecuacion)
    else:
        Simbolo = False
        Ecuacion = Ecuacion + Value
        label_resultado.config(text = Ecuacion)

def memoria(Tipo):
    global Memory, Ecuacion, Simbolo
    match Tipo:
        case "MC":
            Memory = "0"
        case "MR":
            Ecuacion = Ecuacion + Memory
            label_resultado.config(text = Ecuacion)
            Simbolo = False
        case "MS":
            if Simbolo == False:
                x = Calcular()
                Memory = str(x)
        case "MPLUS":
            Memory = Memory + Ecuacion

def Calcular():
    global Ecuacion, resultado
    if Ecuacion:
        try:
            resultado = eval(Ecuacion)
        except:
            label_resultado.config(text = "Error")
            return("0")
        else:
            label_resultado.config(text = resultado)
            return(resultado)

def Delete():
    global Ecuacion, Simbolo
    Ecuacion = Ecuacion[:-1]
    label_resultado.config(text = Ecuacion)
    if Ecuacion:
        if Ecuacion[-1] == "*" or Ecuacion[-1] == "/" or Ecuacion[-1] == "+" or Ecuacion[-1] == "-":
            Simbolo = True
        else:
            Simbolo = False

def UnoEntre():
    global Ecuacion, resultado, Simbolo

    if Simbolo == False:
        if Ecuacion:
            x = Calcular()
            resul = 1/x
            Ecuacion = str(resul)
            label_resultado.config(text = resul)

def MasMenos():
    global Ecuacion, resultado, Simbolo

    if Simbolo == False:
        if Ecuacion:
            x = Calcular()
            resul = -1*x
            Ecuacion = str(resul)
            label_resultado.config(text = resul)

def root():
    global Ecuacion, resultado, Simbolo

    if Simbolo == False:
        if Ecuacion:
            x = Calcular()
            resul = math.sqrt(x)
            Ecuacion = str(resul)
            label_resultado.config(text = resul)

def Borrar():
    global Ecuacion
    Ecuacion = ""
    label_resultado.config(text = "")

label_resultado = tk.Label(Calculadora,width=25, height = 2, font=("Century",30),background = "gray74",text="")
label_resultado.pack()

botonMC = tk.Button(Calculadora,font=("Century",30), text = "MC",width=4,height=1,command=lambda: memoria("MC")).place(x=10,y=115)
botonMR = tk.Button(Calculadora,font=("Century",30), text = "MR",width=4,height=1,command=lambda: memoria("MR")).place(x=120,y=115)
botonMS = tk.Button(Calculadora,font=("Century",30), text = "MS",width=4,height=1,command=lambda: memoria("MS")).place(x=230,y=115)
botonMplus = tk.Button(Calculadora,font=("Century",30), text = "M+",width=4,height=1,command=lambda: memoria("MPLUS")).place(x=340,y=115)
botonsqr = tk.Button(Calculadora,font=("Century",30), text = "sqr",width=4,height=1,command=lambda: root()).place(x=450,y=115)

boton7 = tk.Button(Calculadora,font=("Century",30), text = "7",width=4,height=1,command=lambda: Escribir("7")).place(x=10,y=200)
boton8 = tk.Button(Calculadora,font=("Century",30), text = "8",width=4,height=1,command=lambda: Escribir("8")).place(x=120,y=200)
boton9 = tk.Button(Calculadora,font=("Century",30), text = "9",width=4,height=1,command=lambda: Escribir("9")).place(x=230,y=200)
botonplusminus = tk.Button(Calculadora,font=("Century",30), text = "+-",width=4,height=1,command=lambda: MasMenos()).place(x=340,y=200)
botonpercentage = tk.Button(Calculadora,font=("Century",30), text = "%",width=4,height=1,command=lambda: Escribir("%")).place(x=450,y=200)

boton4 = tk.Button(Calculadora,font=("Century",30), text = "4",width=4,height=1,command=lambda: Escribir("4")).place(x=10,y=285)
boton5 = tk.Button(Calculadora,font=("Century",30), text = "5",width=4,height=1,command=lambda: Escribir("5")).place(x=120,y=285)
boton6 = tk.Button(Calculadora,font=("Century",30), text = "6",width=4,height=1,command=lambda: Escribir("6")).place(x=230,y=285)
botonmulti = tk.Button(Calculadora,font=("Century",30), text = "*",width=4,height=1,command=lambda: Escribir("*")).place(x=340,y=285)
boton1slashx = tk.Button(Calculadora,font=("Century",30), text = "1/x",width=4,height=1,command=lambda: UnoEntre()).place(x=450,y=285)

boton1 = tk.Button(Calculadora,font=("Century",30), text = "1",width=4,height=1,command=lambda: Escribir("1")).place(x=10,y=370)
boton2 = tk.Button(Calculadora,font=("Century",30), text = "2",width=4,height=1,command=lambda: Escribir("2")).place(x=120,y=370)
boton3 = tk.Button(Calculadora,font=("Century",30), text = "3",width=4,height=1,command=lambda: Escribir("3")).place(x=230,y=370)
botonminus = tk.Button(Calculadora,font=("Century",30), text = "-",width=4,height=1,command=lambda: Escribir("-")).place(x=340,y=370)
botonatras = tk.Button(Calculadora,font=("Century",30), text = "DEL",width=4,height=1,command=lambda: Delete()).place(x=450,y=370)

botonborrar = tk.Button(Calculadora,font=("Century",30), text = "C",width=4,height=1,command=lambda: Borrar()).place(x=10,y=455)
boton0 = tk.Button(Calculadora,font=("Century",30), text = "0",width=4,height=1,command=lambda: Escribir("0")).place(x=120,y=455)
botonpoint = tk.Button(Calculadora,font=("Century",30), text = ".",width=4,height=1,command=lambda: Escribir(".")).place(x=230,y=455)
botonplus = tk.Button(Calculadora,font=("Century",30), text = "+",width=4,height=1,command=lambda: Escribir("+")).place(x=340,y=455)
botonequal = tk.Button(Calculadora,font=("Century",30), text = "=",width=4,height=1,command=Calcular).place(x=450,y=455)

Calculadora.mainloop()