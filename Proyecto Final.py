# Proyecto 2
# Joseph Coronado Alvarado
# Alejandro Benavides Juarez

from tkinter import *
from threading import Thread
import time
import pygame
import random
# Musica
pygame.mixer.init()
def play():
    pygame.mixer.music.load("Zanac intro.mp3")
    pygame.mixer.music.play(loops=100)
def stop():
    pygame.mixer.music.stop()

# Pantalla Principal y ventanas
class Ventana():
    def __init__(self, ventana):
        self.ventana = ventana
        self.canvas = Canvas(self.ventana, width=800, height=600, bg="white", highlightbackground="White")
        self.canvas.pack()
        self.canvas.place(x=0, y=0)
        self.alive = True
        self.nombre = ""
        self.PantallaPrincipal()

    def Verificar(self, texto, nivel):

        if texto != "":
            self.nombre = texto
            if nivel == 1:
                return self.primer_nivel()
            elif nivel == 2:
                return self.segundo_nivel()
            elif nivel == 3:
                return self.tercer_nivel()

    def Colision(self, meteorito, nave, colisionando):

        global vida

        coordsMeteorito = self.canvas.bbox(meteorito)
        coordsNave = self.canvas.bbox(nave)

        if coordsMeteorito[0] < coordsNave[1] and coordsMeteorito[2] > coordsNave[0] and coordsMeteorito[1] < \
                coordsNave[3] and coordsMeteorito[3] > coordsNave[1]:

            if colisionando:
                vida -= 1
                self.vida.config(text="Vida: " + str(vida))

                if vida == 0:
                    Agregar(self.nombre + ";" + str(self.scr) + "\n")
                    self.alive = False

                return False


        else:
            return True

    def MovimientoProyectil(self, meteorito, nave):

        x = 5
        y = 5
        colisionando = False

        while (self.alive):

            coordsMeteorito = self.canvas.bbox(meteorito)

            if coordsMeteorito[0] <= 5:
                x = random.randint(1, 5)
                y = random.randint(-5, 5)

            if coordsMeteorito[2] >= 800:
                x = random.randint(-5, -1)
                y = random.randint(-5, 5)

            if coordsMeteorito[1] <= 5:
                y = random.randint(1, 5)
                x = random.randint(-5, 5)

            if coordsMeteorito[3] >= 600:
                y = random.randint(-5, -1)
                x = random.randint(-5, 5)

            self.canvas.move(meteorito, x, y)

            colisionando = self.Colision(meteorito, nave, colisionando)

            self.canvas.update()

            time.sleep(0.01)

    def PantallaPrincipal(self):
        # Variables
        global vida
        vida = 3
        global score
        score = 0

        self.nombre = ""
        self.alive = False
        self.scr = 0

        # Fondo
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="white")
        bg = PhotoImage(file="fondo.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(420, 80, text="Space Souls III", font=("Airstrike", 35), fill="#FFF8E7")
        self.canvas.create_text(415, 120, text="Digite su Nombre", font=("Airstrike", 25), fill="gainsboro")
        # Entry del nombre
        un_entry = Entry(self.ventana, font=("Airstrike", 30), width=10, fg="black")
        un_window = self.canvas.create_window(272, 135, anchor="nw", window=un_entry)
        # Boton Nivel 1
        self.boton_start = Button(self.canvas, text="Nivel 1", font=("Airstrike", 25),
                                  command=lambda: self.Verificar(un_entry.get(), 1))
        self.boton_start.place(x=75, y=300)
        # Boton Nivel 2
        self.boton_start = Button(self.canvas, text="Nivel 2", font=("Airstrike", 25),
                                  command=lambda: self.Verificar(un_entry.get(), 2))
        self.boton_start.place(x=335, y=300)
        # Boton Nivel 3
        self.boton_start = Button(self.canvas, text="Nivel 3", font=("Airstrike", 25),
                                  command=lambda: self.Verificar(un_entry.get(), 3))
        self.boton_start.place(x=580, y=300)
        # Botones de Musica
        # Boton Musica Encendida
        self.boton_on = Button(self.canvas, text="🔊 ON", font=("Airstrike", 10), command=play)
        self.boton_on.place(x=650, y=10)
        # Boton Musica Apagada
        self.boton_off = Button(self.canvas, text="🔊 OFF", font=("Airstrike", 10), command=stop)
        self.boton_off.place(x=700, y=10)
        # Boton pagina de puntajes
        self.boton_start = Button(self.canvas, text="Best Scores", font=("Airstrike", 25), command=self.scores)
        self.boton_start.place(x=305, y=480)
        # Boton pagina de creditos
        self.boton_credits = Button(self.canvas, text="Creditos", font=("Airstrike", 25), command=self.creditos)
        self.boton_credits.place(x=20, y=480)
        # Boton Quitar juego
        self.boton_quitButton = Button(self.canvas, text="Salir", font=("Airstrike", 25), command=self.quitar_juego)
        self.boton_quitButton.place(x=650, y=480)
        self.ventana.mainloop()

        # ----------------------------------------- Nivel 1 --------------------------------------------------------------

    def Cambiar2(self):
        if self.sec1 >= 60:
            return self.segundo_nivel()

        # Nivel 1

    def primer_nivel(self):
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="White")
        self.canvas.place(x=-5, y=0)
        bg = PhotoImage(file="space.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 15), bg="Yellow", command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)
        self.boton0 = Button(self.canvas, text="Next", font=("Airstrike", 15), bg="Yellow", command=self.Cambiar2)

        self.alive = True

        # Botones de Musica
        # Boton Musica Encendida
        self.boton_on = Button(self.canvas, text="🔊 ON", font=("Airstrike", 10), command=play)
        self.boton_on.place(x=650, y=10)
        # Boton Musica Apagada
        self.boton_off = Button(self.canvas, text="🔊 OFF", font=("Airstrike", 10), command=stop)
        self.boton_off.place(x=700, y=10)

        # Imagen de la nave
        self.nave_jugador = PhotoImage(file="nave.png")
        self.nave = self.canvas.create_image(350, 430, anchor=NW, image=self.nave_jugador)

        # Imagen del meteorito 1
        self.meteor_1 = PhotoImage(file="meteor2.gif")
        self.meteor1 = self.canvas.create_image(315, 350, anchor=NW, image=self.meteor_1)

        #  Barra de vida
        self.progresbar = LabelFrame(self.canvas, width=800, height=25, background="black")
        self.progresbar.place(x=0, y=800)
        self.vida = Label(self.canvas, text="Vida: " + str(vida), font=("Airstrike", 11))
        self.vida.place(x=5, y=550)

        # Tiempo
        self.Label_time = Label(self.canvas, text="Time:", font=("Airstrike", 11))
        self.Label_time.place(x=100, y=550)

        self.segundos1 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.segundos1.place(x=145, y=550)

        self.sec1 = 0
        self.vidaPlayerLv1 = 3

        #  Puntaje
        self.score_label = Label(self.canvas, text="Score:", font=("Airstrike", 11))
        self.score_label.place(x=190, y=550)

        self.score1 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.score1.place(x=250, y=550)

        self.vidaPlayerLv1 = 3

        # Movimientos de la nave
        def left(event):
            x = -12
            y = 0
            self.canvas.move(self.nave, x, y)

        def right(event):
            x = 12
            y = 0
            self.canvas.move(self.nave, x, y)

        def up(event):
            x = 0
            y = -12
            self.canvas.move(self.nave, x, y)

        def down(event):
            x = 0
            y = 12
            self.canvas.move(self.nave, x, y)

        # LLamadas a los movimientos
        self.ventana.bind("<Left>", left)
        self.ventana.bind("<Right>", right)
        self.ventana.bind("<Up>", up)
        self.ventana.bind("<Down>", down)

        time = Thread(target=self.TimeLevel1)
        time.start()
        score = Thread(target=self.puntaje1)
        score.start()
        hiloMP2 = Thread(target=self.MovimientoProyectil, args=(self.meteor1, self.nave))
        hiloMP2.start()

        self.ventana.mainloop()

        # Tiempo del nivel 1

    def TimeLevel1(self):
        if not self.alive:
            return 0
        elif self.sec1 >= 60:
            self.alive = False
            self.boton0.place(x=0, y=40)
        self.sec1 += 1
        time.sleep(1)
        self.segundos1.config(text=str(self.sec1))
        return self.TimeLevel1()

        # Score

    def puntaje1(self):
        if not self.alive:
            return 0
        self.scr += 1
        time.sleep(1)
        self.score1.config(text=str(self.scr))
        return self.puntaje1()
        # ----------------------------------------  Nivel 2 --------------------------------------------------------
    def Cambiar3(self):
        if self.sec2 >= 60:
            return self.tercer_nivel()
        # Nivel 2
    def segundo_nivel(self):
        self.alive = True
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="White")
        self.canvas.place(x=-5, y=0)
        bg = PhotoImage(file="space.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 15), bg="Yellow",command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)
        self.boton0 = Button(self.canvas, text="Next", font=("Airstrike", 15), bg="Yellow", command=self.Cambiar3)

        self.alive = True

        # Botones de Musica
        # Boton Musica Encendida
        self.boton_on = Button(self.canvas, text="🔊 ON", font=("Airstrike", 10), command=play)
        self.boton_on.place(x=650, y=10)
        # Boton Musica Apagada
        self.boton_off = Button(self.canvas, text="🔊 OFF", font=("Airstrike", 10), command=stop)
        self.boton_off.place(x=700, y=10)

        # Imagen de la nave
        self.nave_jugador2 = PhotoImage(file="nave.png")
        self.nave = self.canvas.create_image(350, 430, anchor=NW, image=self.nave_jugador2)

        # Imagen del meteorito 1
        self.meteor_1 = PhotoImage(file="meteor.gif")
        self.meteor1 = self.canvas.create_image(500, 100, anchor=NW, image=self.meteor_1)

        # Imagen del meteorito 2
        self.meteor_2 = PhotoImage(file="meteor2.gif")
        self.meteor2 = self.canvas.create_image(600, 350, anchor=NW, image=self.meteor_2)

        #  Barra de vida
        self.progresbar = LabelFrame(self.canvas, width=800, height=25, background="black")
        self.progresbar.place(x=0, y=800)
        self.vida = Label(self.canvas, text="Vida: " + str(vida), font=("Airstrike", 11))
        self.vida.place(x=5, y=550)

        # Tiempo
        self.Label_time = Label(self.canvas, text="Time:", font=("Airstrike", 11))
        self.Label_time.place(x=100, y=550)

        self.segundos2 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.segundos2.place(x=145, y=550)

        self.sec2 = 0
        self.vidaPlayerLv2 = 3

        #  Puntaje
        self.score_label = Label(self.canvas, text="Score:", font=("Airstrike", 11))
        self.score_label.place(x=190, y=550)

        self.score2 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.score2.place(x=250, y=550)

        self.vidaPlayerLv1 = 3

        # Movimientos de la nave
        def left(event):
            x = -14
            y = 0
            self.canvas.move(self.nave, x, y)

        def right(event):
            x = 14
            y = 0
            self.canvas.move(self.nave, x, y)

        def up(event):
            x = 0
            y = -14
            self.canvas.move(self.nave, x, y)

        def down(event):
            x = 0
            y = 14
            self.canvas.move(self.nave, x, y)



        # LLamadas a los movimientos
        self.ventana.bind("<Left>", left)
        self.ventana.bind("<Right>", right)
        self.ventana.bind("<Up>", up)
        self.ventana.bind("<Down>", down)

        time = Thread(target=self.TimeLevel2)
        time.start()
        score = Thread(target=self.puntaje2)
        score.start()
        hiloMP2 = Thread(target=self.MovimientoProyectil, args=(self.meteor1, self.nave))
        hiloMP2.start()
        hiloMP1 = Thread(target=self.MovimientoProyectil, args=(self.meteor2, self.nave))
        hiloMP1.start()

        self.ventana.mainloop()

        # Tiempo del nivel 2

    def TimeLevel2(self):
        if not self.alive:
            return 0
        elif self.sec2 >= 60:
            self.alive = False
            self.boton0.place(x=0, y=40)
        self.sec2 += 1
        time.sleep(1)
        self.segundos2.config(text=str(self.sec2))
        return self.TimeLevel2()

        # Score

    def puntaje2(self):
        if not self.alive:
            return 0
        self.scr += 2.5
        time.sleep(1)
        self.score2.config(text=str(self.scr))
        return self.puntaje2()

        # ------------------------------------------- Nivel 3 ----------------------------------------------
        # Nivel 3

    def tercer_nivel(self):
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="White")
        self.canvas.place(x=-5, y=0)
        bg = PhotoImage(file="space.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 15), bg="Yellow", command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)
        # Botones de Musica
        # Boton Musica Encendida
        self.boton_on = Button(self.canvas, text="🔊 ON", font=("Airstrike", 10), command=play)
        self.boton_on.place(x=650, y=10)
        # Boton Musica Apagada
        self.boton_off = Button(self.canvas, text="🔊 OFF", font=("Airstrike", 10), command=stop)
        self.boton_off.place(x=700, y=10)
        self.alive = True
        # Imagen de la nave
        self.nave_jugador3 = PhotoImage(file="nave.png")
        self.nave = self.canvas.create_image(350, 430, anchor=NW, image=self.nave_jugador3)

        # Imagen del meteorito 1
        self.meteor_1 = PhotoImage(file="meteor.gif")
        self.meteor1 = self.canvas.create_image(100, 400, anchor=NW, image=self.meteor_1)

        # Imagen del meteorito 2
        self.meteor_2 = PhotoImage(file="meteor2.gif")
        self.meteor2 = self.canvas.create_image(600, 350, anchor=NW, image=self.meteor_2)

        # Imagen del meteorito 3
        self.meteor_3 = PhotoImage(file="meteor.gif")
        self.meteor3 = self.canvas.create_image(300, 200, anchor=NW, image=self.meteor_3)

        #  Barra de vida
        self.progresbar = LabelFrame(self.canvas, width=800, height=25, background="black")
        self.progresbar.place(x=0, y=800)
        self.vida = Label(self.canvas, text="Vida: " + str(vida), font=("Airstrike", 11))
        self.vida.place(x=5, y=550)

        # Tiempo
        self.Label_time = Label(self.canvas, text="Time:", font=("Airstrike", 11))
        self.Label_time.place(x=100, y=550)

        self.segundos3 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.segundos3.place(x=145, y=550)

        self.sec3 = 0
        self.vidaPlayerLv3 = 3

        #  Puntaje
        self.score_label = Label(self.canvas, text="Score:", font=("Airstrike", 11))
        self.score_label.place(x=190, y=550)

        self.score3 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.score3.place(x=250, y=550)
        self.vidaPlayerLv1 = 3

        # Movimientos de la nave
        def left(event):
            x = -16
            y = 0
            self.canvas.move(self.nave, x, y)

        def right(event):
            x = 16
            y = 0
            self.canvas.move(self.nave, x, y)

        def up(event):
            x = 0
            y = -16
            self.canvas.move(self.nave, x, y)

        def down(event):
            x = 0
            y = 16
            self.canvas.move(self.nave, x, y)



        # LLamadas a los movimientos
        self.ventana.bind("<Left>", left)
        self.ventana.bind("<Right>", right)
        self.ventana.bind("<Up>", up)
        self.ventana.bind("<Down>", down)

        time = Thread(target=self.TimeLevel3)
        time.start()
        score = Thread(target=self.puntaje3)
        score.start()
        hiloMP2 = Thread(target=self.MovimientoProyectil, args=(self.meteor1, self.nave))
        hiloMP2.start()
        hiloMP1 = Thread(target=self.MovimientoProyectil, args=(self.meteor2, self.nave))
        hiloMP1.start()
        hiloMP3 = Thread(target=self.MovimientoProyectil, args=(self.meteor3, self.nave))
        hiloMP3.start()


        self.ventana.mainloop()

        # Tiempo del nivel 3

    def TimeLevel3(self):
        if self.alive:
            return 0
        self.sec3 += 1
        time.sleep(1)
        self.segundos3.config(text=str(self.sec3))
        return self.TimeLevel3()

        # Score

    def puntaje3(self):
        if self.alive:
            return 0
        self.scr += 5
        time.sleep(1)
        self.score3.config(text=str(self.scr))
        return self.puntaje3()

        #########################################################################################################################################
        # Puntajes

    def scores(self):
        Escribir(GenerarLista(quicksort(GenerarMatriz(Leer()))))
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="White")
        bg = PhotoImage(file="space.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.canvas.place(x=-5, y=0)
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 15), bg="Yellow",command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)

        # Imagen del meme
        self.meme = PhotoImage(file="nopuedeser.png")
        self.hehe = self.canvas.create_image(250, 65, anchor=NW, image=self.meme)

        self.ventana.mainloop()

        #########################################################################################################################################
        # Creditos

    def creditos(self):
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="White")
        bg = PhotoImage(file="space.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.canvas.place(x=-5, y=0)
        self.canvas.create_text(400, 260,
                                text="   Creado en Costa Rica\n\n   Tecnologico De Costa Rica \n\n   Ingenieria en Computadores \n\n   2021 Grupo 03 \n\n    Leonardo Araya \n\n    Ver.1.0 \n\n    Joseph Coronado Alvarado \n\n    Alejandro Benavides Juarez \n\n    Tkinter ",
                                font=("Airstrike", 25), fill="green")
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 15), bg="Yellow",
                             command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)
        self.ventana.mainloop()

        ######################################################################################################################################
        # Quitar juego

    def quitar_juego(self):
        self.ventana.destroy()
        self.ventana.mainloop()

def Leer():

    archivo = open("puntajes.txt","r")
    lines = archivo.readlines()
    archivo.close()
    return lines

def GenerarMatriz(lines):

    temp = []

    for i in lines:
        aux = i.split(";")
        temp += [[aux[0],float(aux[1])]]

    return temp

def quicksort(lista):

    if len(lista) == 1 or len(lista) == 0:
        return lista
    else:
        pivot = lista[0][1]
        i = 0
        for j in range(len(lista) - 1):
            if lista[j + 1][1] > pivot:
                lista[j + 1], lista[i + 1] = lista[i + 1], lista[j + 1]
                i += 1
        lista[0], lista[i] = lista[i], lista[0]
        first_part = quicksort(lista[:i])
        second_part = quicksort(lista[i + 1:])
        first_part.append(lista[i])
        return first_part + second_part

def GenerarLista(matriz):

    lista = []

    for i in matriz:

        lista.append(i[0] + ";" +  str(i[1]) + "\n")

    return lista

def Escribir(lista):

    archivo = open("puntajes.txt","w")
    archivo.writelines(lista)
    archivo.close()

def Agregar(puntaje): #Formato = Nombre:Puntaje\n
    archivo = open("puntajes.txt", "a")
    archivo.writelines(puntaje)
    archivo.close()


# Fin del programa
ventana = Tk()
ventana.title("Proyecto Taller")
ventana.minsize(800, 600)
ventana.resizable(width=NO, height=NO)
ventana.config(bg="Black")

miObjetoVentanas = Ventana(ventana)

ventana.mainloop()