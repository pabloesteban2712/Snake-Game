# SNAKE GAME

import turtle
import time
import random

posponer = 0.1  # Que empiece un poco más tarde

# Marcador
score = 0
high_score = 0

# Config ventana
wn = turtle.Screen()  # Abrimos la interfaz
wn.title("Snake Game")  # Titulo
wn.bgcolor("black")  # Color de fondo
wn.setup(width=600, height=600)  # Tamaño en pixeles
wn.tracer(0)  # Permite un control manual

# Cabeza serpiente
cabeza = turtle.Turtle()  # Creamos el elemento grafico de la serpiente
cabeza.speed(0)  # Velocidad
cabeza.shape("square")  # Forma del objeto creado
cabeza.color("green")
cabeza.penup()
cabeza.goto(0, 0)  # 0,0 es el centro de la pantalla, ahí comienza el juego
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()  # Creamos el elemento grafico de la serpiente
comida.speed(0)  # Velocidad
comida.shape("circle")  # Forma del objeto creado
comida.color("red")
comida.penup()
comida.goto(0, 100)

# Cuerpo serpiente
segmentos = []

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))

# Funciones de dirección
def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

# Movimiento de la cabeza
def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

# Bucle principal
while True:
    wn.update()  # Actualiza la ventana

    # Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        # Reiniciamos el cuerpo
        for segmento in segmentos:
            segmento.goto(1000, 1000)
        segmentos.clear()  # Vaciamos la lista
        score = 0  # Reiniciamos el marcador

    # Colisiones comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        # Agregar un nuevo segmento al cuerpo
        cuerpo = turtle.Turtle()
        cuerpo.speed(0)
        cuerpo.shape("square")
        cuerpo.color("darkgreen")
        cuerpo.penup()
        segmentos.append(cuerpo)

        # Actualizar marcador
        score += 10
        if score > high_score:
            high_score = score

    # Actualizar el marcador en pantalla
    texto.clear()
    texto.write("Score: {}    High Score: {}".format(score, high_score), 
                align="center", font=("Courier", 24, "normal"))

    # Mover cuerpo serpiente
    for index in range(len(segmentos) - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if len(segmentos) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    movimiento()

    # Colisiones cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            # Reiniciamos el cuerpo
            for segmento in segmentos:
                segmento.goto(1000, 1000)
            segmentos.clear()
            score = 0  # Reiniciamos el marcador

    time.sleep(posponer)

wn.mainloop()