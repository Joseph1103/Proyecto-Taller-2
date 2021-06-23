from tkinter import*

class Proyectiles:
    def __init__(self,canvas,x,y,diameter,xvelocidad,yvelocidad,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter, fill=color)
        self.xvelocidad = xvelocidad
        self.yvelocidad = yvelocidad

    def move(self):
        cordenadas = self.canvas.coords(self.image)
        print(cordenadas)

        self.canvas.move(self.image,self.yvelocidad, self.xvelocidad)