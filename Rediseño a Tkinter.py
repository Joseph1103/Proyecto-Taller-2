# Proyecto 2 Rediseñado en Tkinter
# Joseph Coronado Alvarado
# Alejandro Benavides Juarez

from tkinter import *
# from threading import Thread
# import time

# Pantalla Principal y ventanas
class Ventana():
    def __init__(self, ventana):
        self.ventana = ventana
        self.canvas = Canvas(self.ventana, width=800, height=600, bg="white", highlightbackground="White")
        self.canvas.pack()
        self.canvas.place(x=0, y=0)
        self.PantallaPrincipal()

    def PantallaPrincipal(self):
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
        self.boton_start = Button(self.canvas, text="Nivel 2", font=("Airstrike", 25))  # command=self.first_level)
        self.boton_start.place(x=335, y=300)
    # Boton Nivel 3
        self.boton_start = Button(self.canvas, text="Nivel 3", font=("Airstrike", 25))  # command=self.first_level)
        self.boton_start.place(x=580, y=300)
    # Boton pagina de creditos
        self.boton_credits = Button(self.canvas, text="Creditos", font=("Airstrike", 25))# command=self.credits)
        self.boton_credits.place(x=20, y=480)
    # Boton Quitar juego
        self.boton_quitButton = Button(self.canvas, text="Salir", font=("Airstrike", 25))#  command=self.quitGame)
        self.boton_quitButton.place(x=650, y=480)
        self.ventana.mainloop()

    # Nivel 1
    def primer_nivel(self):
        self.canvas = Canvas(self.ventana, width=800, height=600, highlightbackground="White")
        self.canvas.place(x=-5, y=0)
        bg = PhotoImage(file="space.png")
        self.canvas.create_image(0, 0, image=bg, anchor="nw")
        self.boton2 = Button(self.canvas, text="Menu", font=("Airstrike", 10), bg="Yellow",command=self.PantallaPrincipal)
        self.boton2.place(x=0, y=0)
        self.ventana.mainloop()



ventana = Tk()
ventana.title("Proyecto Taller")
ventana.minsize(800, 600)
ventana.resizable(width=NO, height=NO)
ventana.config(bg="Black")

miObjetoVentanas = Ventana(ventana)

ventana.mainloop()