import tkinter as tk
from tkinter import messagebox
import random

Puzzle = tk.Tk()
Puzzle.title("Slider")
Puzzle.geometry("785x570")
Puzzle.iconbitmap("Puzzle\Puzzle.ico")
Puzzle.resizable(False,False)
Puzzle.config(background="RoyalBlue3")

GameClear = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",""]
Game = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",""]
current = 0

GameStatus = False

Estado0 = [1,4]
Estado1 = [0,2,5]
Estado2 = [1,3,6]
Estado3 = [2,7]
Estado4 = [0,5,8]
Estado5 = [1,4,6,9]
Estado6 = [2,5,7,10]
Estado7 = [3,6,11]
Estado8 = [4,9,12]
Estado9 = [5,8,10,13]
Estado10 = [6,9,11,14]
Estado11 = [7,10,15]
Estado12 = [8,13]
Estado13 = [9,12,14]
Estado14 = [10,13,15]
Estado15 = [11,14]

def GameStart():
    global Game, Botones, current, GameStatus, Botones
    if current >= 0 and current < 16:
        Botones[current].config(bg = "red3")

    LabelGanar.config(text="Esperando",bg = "aquamarine")
    random.shuffle(Game)
    for i, boton in enumerate(Botones):
        texto = f"{Game[i]}"
        if texto == "":
            current = i
            Botones[i].config(bg = "RoyalBlue3")    
        boton.config(text=texto, fg="peach puff")   
    print (current)
    GameStatus = True

def move(move):
    global current, Game, GameStatus
    
    if GameStatus:
        match move:
            case 0:
                if current in Estado0:
                    Act(move, current)
            case 1:
                if current in Estado1:
                    Act(move, current)
            case 2:
                if current in Estado2:
                    Act(move, current)
            case 3:
                if current in Estado3:
                    Act(move, current)
            case 4:
                if current in Estado4:
                    Act(move, current)
            case 5:
                if current in Estado5:
                    Act(move, current)
            case 6:
                if current in Estado6:
                    Act(move, current)
            case 7:
                if current in Estado7:
                    Act(move, current)
            case 8:
                if current in Estado8:
                    Act(move, current)
            case 9:
                if current in Estado9:
                    Act(move, current)
            case 10:
                if current in Estado10:
                    Act(move, current)
            case 11:
                if current in Estado11:
                    Act(move, current)
            case 12:
                if current in Estado12:
                    Act(move, current)
            case 13:
                if current in Estado13:
                    Act(move, current)
            case 14:
                if current in Estado14:
                    Act(move, current)
            case 15:
                if current in Estado15:
                    Act(move, current)

def Act(Valor1,Valor2):
    global Game, Botones, current
    current = Valor1
    Botones[Valor1].config(text = "",bg = "RoyalBlue3")
    Botones[Valor2].config(text = f"{Game[Valor1]}",bg = "red3")
    Game[Valor1], Game[Valor2] = Game[Valor2], Game[Valor1]
    Check()

def Check():
    global Game, GameClear, GameStatus
    if Game == GameClear:
        GameStatus = False
        LabelGanar.config(text="Ganaste",bg = "gold")
    else:
        return(False)



boton1 = tk.Button(Puzzle,font=("Century",30), bg = "red3", width=5,height=2,command=lambda: move(0))
boton1.place(x=5,y=10)
boton2 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(1))
boton2.place(x=146,y=10)
boton3 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(2))
boton3.place(x=287,y=10)
boton4 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(3))
boton4.place(x=428,y=10)

boton5 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(4))
boton5.place(x=5,y=145)
boton6 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(5))
boton6.place(x=146,y=145)
boton7 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(6))
boton7.place(x=287,y=145)
boton8 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(7))
boton8.place(x=428,y=145)

boton9 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(8))
boton9.place(x=5,y=287)
boton10 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(9))
boton10.place(x=146,y=287)
boton11 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(10))
boton11.place(x=287,y=287)
boton12 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(11))
boton12.place(x=428,y=287)

boton13 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(12))
boton13.place(x=5,y=428)
boton14 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(13))
boton14.place(x=146,y=428)
boton15 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(14))
boton15.place(x=287,y=428)
boton16 = tk.Button(Puzzle,font=("Century",30),bg = "red3", width=5,height=2,command=lambda: move(15))
boton16.place(x=428,y=428)

LabelGanar = tk.Label(Puzzle,font=("Century",30), text = "Esperando",width=8,height=1,bg = "aquamarine")
LabelGanar.place(x=569,y=10)
botonRestart = tk.Button(Puzzle,font=("Century",30), text = "New Game",width=8,height=1,bg = "aquamarine", command=lambda: GameStart()).place(x=569,y=475)

Botones = [boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16]

Puzzle.mainloop()