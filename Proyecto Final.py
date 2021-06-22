# Proyecto 2 Rediseñado en Tkinter
# Joseph Coronado Alvarado
# Alejandro Benavides Juarez

from tkinter import *
from threading import Thread
import time

# Pantalla Principal y ventanas
class Ventana():
    def __init__(self, ventana):
        self.ventana = ventana
        self.canvas = Canvas(self.ventana, width=800, height=600, bg="white", highlightbackground="White")
        self.canvas.pack()
        self.canvas.place(x=0, y=0)
        self.alive = False
        self.PantallaPrincipal()

    def PantallaPrincipal(self):
    # Variables
        global vida
        vida = 3
        global score
        score = 0
    # Fondo
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="white")
        bg = PhotoImage(file="fondo.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(420, 80, text="Dodge Space", font=("Airstrike", 35), fill="#FFF8E7")
        self.canvas.create_text(415, 120, text="Digite su Nombre", font=("Airstrike", 25), fill="gainsboro")
    # Entry del nombre
        un_entry = Entry(self.ventana, font=("Airstrike", 30), width=10, fg="black")
        un_window = self.canvas.create_window(272, 135, anchor="nw", window=un_entry)
    # Boton Nivel 1
        self.boton_start = Button(self.canvas, text="Nivel 1", font=("Airstrike", 25), command=self.primer_nivel)
        self.boton_start.place(x=75, y=300)
    # Boton Nivel 2
        self.boton_start = Button(self.canvas, text="Nivel 2", font=("Airstrike", 25) , command=self.segundo_nivel)
        self.boton_start.place(x=335, y=300)
    # Boton Nivel 3
        self.boton_start = Button(self.canvas, text="Nivel 3", font=("Airstrike", 25), command=self.tercer_nivel)
        self.boton_start.place(x=580, y=300)
    # Boton pagina de creditos
        self.boton_credits = Button(self.canvas, text="Creditos", font=("Airstrike", 25), command=self.creditos)
        self.boton_credits.place(x=20, y=480)
    # Boton Quitar juego
        self.boton_quitButton = Button(self.canvas, text="Salir", font=("Airstrike", 25), command=self.quitar_juego)
        self.boton_quitButton.place(x=650, y=480)
        self.ventana.mainloop()

    # Nivel 1
    def primer_nivel(self):
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="White")
        self.canvas.place(x=-5, y=0)
        bg = PhotoImage(file="space.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.boton2 = Button(self.canvas, text="Menu",  font=("Airstrike", 15), bg="Yellow",command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)

    # Imagen de la nave
        self.nave_jugador = PhotoImage(file="nave.png")
        self.nave = self.canvas.create_image(350, 430, anchor=NW, image=self.nave_jugador)

    # Imagen del meteorito 1
        self.meteor_1 = PhotoImage(file="meteor.gif")
        self.meteor = self.canvas.create_image(750, 100, anchor=NW, image=self.meteor_1)

    # Imagen del meteorito 2
        self.meteor_2 = PhotoImage(file="meteor2.gif")
        self.meteor = self.canvas.create_image(315, 350, anchor=NW, image=self.meteor_2)

    #  Barra de vida
        self.progresbar = LabelFrame(self.canvas, width=800, height=25, background="black")
        self.progresbar.place(x=0, y=800)
        self.vida = Label(self.canvas, text="Vida: " + str(vida), font=("Airstrike", 11))
        self.vida.place(x=5, y=550)

    # Tiempo
        self.Label_time = Label(self.canvas, text="Time:",font=("Airstrike", 11))
        self.Label_time.place(x=100, y=550)

        self.segundos1 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.segundos1.place(x=145, y=550)

        self.sec1 = 0
        self.vidaPlayerLv1 = 3
        self.alive = False

    #  Puntaje
        self.score_label = Label(self.canvas, text="Score:", font=("Airstrike", 11))
        self.score_label.place(x=190, y=550)

        self.score1 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.score1.place(x=250, y=550)

        self.scr1 = 0
        self.vidaPlayerLv1 = 3
        self.alive = False

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


            self.ventana.mainloop()

    # LLamadas a los movimientos
        self.ventana.bind("<Left>", left)
        self.ventana.bind("<Right>", right)
        self.ventana.bind("<Up>", up)
        self.ventana.bind("<Down>", down)

        time = Thread(target=self.TimeLevel1)
        time.start()
        score = Thread(target=self.puntaje1)
        score.start()

        self.ventana.mainloop()

    # Tiempo del nivel 1
    def TimeLevel1(self):
        if self.alive:
            return 0
        self.sec1 += 1
        time.sleep(1)
        self.segundos1.config(text=str(self.sec1))
        return self.TimeLevel1()

    # Score
    def puntaje1(self):
        if self.alive:
            return 0
        self.scr1 += 1
        time.sleep(1)
        self.score1.config(text=str(self.scr1))
        return self.puntaje1()

    # Nivel 2
    def segundo_nivel(self):
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="White")
        self.canvas.place(x=-5, y=0)
        bg = PhotoImage(file="space.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 15), bg="Yellow",command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)

    # Imagen de la nave
        self.nave_jugador2 = PhotoImage(file="nave.png")
        self.nave = self.canvas.create_image(350, 430, anchor=NW, image=self.nave_jugador2)

    # Imagen del meteorito 1
        self.meteor_1 = PhotoImage(file="meteor.gif")
        self.meteor = self.canvas.create_image(50, 100, anchor=NW, image=self.meteor_1)

    # Imagen del meteorito 2
        self.meteor_2 = PhotoImage(file="meteor2.gif")
        self.meteor = self.canvas.create_image(210, 350, anchor=NW, image=self.meteor_2)

    # Imagen del meteorito 3
        self.meteor_3 = PhotoImage(file="meteor2.gif")
        self.meteor = self.canvas.create_image(500, 200, anchor=NW, image=self.meteor_3)

    #  Barra de vida
        self.progresbar = LabelFrame(self.canvas, width=800, height=25, background="black")
        self.progresbar.place(x=0, y=800)
        self.vida = Label(self.canvas, text="Vida: " + str(vida), font=("Airstrike", 11))
        self.vida.place(x=5, y=550)

    # Tiempo
        self.Label_time = Label(self.canvas, text="Time:",font=("Airstrike", 11))
        self.Label_time.place(x=100, y=550)

        self.segundos2 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.segundos2.place(x=145, y=550)

        self.sec2 = 0
        self.vidaPlayerLv2 = 3
        self.alive = False

    #  Puntaje
        self.score_label = Label(self.canvas, text="Score:", font=("Airstrike", 11))
        self.score_label.place(x=190, y=550)

        self.score2 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.score2.place(x=250, y=550)

        self.scr2 = 0
        self.vidaPlayerLv1 = 3
        self.alive = False

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

            self.ventana.mainloop()

        # LLamadas a los movimientos
        self.ventana.bind("<Left>", left)
        self.ventana.bind("<Right>", right)
        self.ventana.bind("<Up>", up)
        self.ventana.bind("<Down>", down)

        time = Thread(target=self.TimeLevel2)
        time.start()
        score = Thread(target=self.puntaje2)
        score.start()

        self.ventana.mainloop()

        # Tiempo del nivel 2
    def TimeLevel2(self):
            if self.alive:
                return 0
            self.sec2 += 1
            time.sleep(1)
            self.segundos2.config(text=str(self.sec2))
            return self.TimeLevel2()

    # Score
    def puntaje2(self):
        if self.alive:
            return 0
        self.scr2 += 2.5
        time.sleep(1)
        self.score2.config(text=str(self.scr2))
        return self.puntaje2()

    # Nivel 3
    def tercer_nivel(self):
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="White")
        self.canvas.place(x=-5, y=0)
        bg = PhotoImage(file="space.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 15), bg="Yellow", command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)

    # Imagen de la nave
        self.nave_jugador3 = PhotoImage(file="nave.png")
        self.nave = self.canvas.create_image(350, 430, anchor=NW, image=self.nave_jugador3)

    # Imagen del meteorito 1
        self.meteor_1 = PhotoImage(file="meteor.gif")
        self.meteor = self.canvas.create_image(100, 400, anchor=NW, image=self.meteor_1)

    # Imagen del meteorito 2
        self.meteor_2 = PhotoImage(file="meteor2.gif")
        self.meteor = self.canvas.create_image(600, 350, anchor=NW, image=self.meteor_2)

    # Imagen del meteorito 3
        self.meteor_3 = PhotoImage(file="meteor2.gif")
        self.meteor = self.canvas.create_image(300, 200, anchor=NW, image=self.meteor_3)

    # Imagen del meteorito 1
        self.meteor_4 = PhotoImage(file="meteor.gif")
        self.meteor = self.canvas.create_image(450, 500, anchor=NW, image=self.meteor_4)

    #  Barra de vida
        self.progresbar = LabelFrame(self.canvas, width=800, height=25, background="black")
        self.progresbar.place(x=0, y=800)
        self.vida = Label(self.canvas, text="Vida: " + str(vida), font=("Airstrike", 11))
        self.vida.place(x=5, y=550)

    # Tiempo
        self.Label_time = Label(self.canvas, text="Time:",font=("Airstrike", 11))
        self.Label_time.place(x=100, y=550)

        self.segundos3 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.segundos3.place(x=145, y=550)

        self.sec3 = 0
        self.vidaPlayerLv3 = 3
        self.alive = False

    #  Puntaje
        self.score_label = Label(self.canvas, text="Score:", font=("Airstrike", 11))
        self.score_label.place(x=190, y=550)

        self.score3 = Label(self.canvas, text="", font=("Airstrike", 11))
        self.score3.place(x=250, y=550)

        self.scr3 = 0
        self.vidaPlayerLv1 = 3
        self.alive = False

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


            self.ventana.mainloop()

    # LLamadas a los movimientos
        self.ventana.bind("<Left>", left)
        self.ventana.bind("<Right>", right)
        self.ventana.bind("<Up>", up)
        self.ventana.bind("<Down>", down)

        time = Thread(target=self.TimeLevel3)
        time.start()
        score = Thread(target=self.puntaje3)
        score.start()

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
        self.scr3 += 5
        time.sleep(1)
        self.score3.config(text=str(self.scr3))
        return self.puntaje3()

#########################################################################################################################################
# Creditos
    def creditos(self):
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="White")
        bg = PhotoImage(file="space.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.canvas.place(x=-5, y=0)
        self.canvas.create_text(400, 260, text="   Creado en Costa Rica\n\n   Tecnologico De Costa Rica \n\n   Ingenieria en Computadores \n\n   2021 Grupo 03 \n\n    Leonardo Araya \n\n    Ver.1.0 \n\n    Joseph Coronado Alvarado \n\n    Alejandro Benavides Juarez \n\n    Tkinter ", font=("Airstrike", 25), fill="green")
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 15), bg="Yellow", command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)
        self.ventana.mainloop()

######################################################################################################################################
# Quitar juego
    def quitar_juego(self):
        self.ventana.destroy()
        self.ventana.mainloop()

# Fin del programa
ventana = Tk()
ventana.title("Proyecto Taller")
ventana.minsize(800, 600)
ventana.resizable(width=NO, height=NO)
ventana.config(bg="Black")

miObjetoVentanas = Ventana(ventana)

ventana.mainloop()