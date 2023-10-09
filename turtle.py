import turtle


wn = turtle.Screen()
wn.title = ("TOP GIOCO EU")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# piastra sx
piastra_sx = turtle.Turtle()
# velocita di animazione impostata al massimo
piastra_sx.speed(0)
piastra_sx.shape("square")
piastra_sx.color("white")
piastra_sx.shapesize(stretch_wid=10, stretch_len=1)
piastra_sx.penup()
# posizione di partenza dell'oggetto
piastra_sx.goto(-350, 0)


# piastra dx
piastra_dx = turtle.Turtle()
# velocita di animazione impostata al massimo
piastra_dx.speed(0)
piastra_dx.shape("square")
piastra_dx.color("white")
piastra_dx.shapesize(stretch_wid=10, stretch_len=1)
piastra_dx.penup()
# posizione di partenza dell'oggetto
piastra_dx.goto(350, 0)

# palla

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("grey")
ball.goto(0, 0)
ball.penup()
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)


def piastra_sx_su():
    # prendo la coordinata y
    y = piastra_sx.ycor()
    y += 20
    piastra_sx.sety(y)


def piastra_sx_giu():
    y = piastra_sx.ycor()
    y += -20
    piastra_sx.sety(y)


def piastra_dx_su():
    # prendo la coordinata y
    y = piastra_dx.ycor()
    y += 20
    piastra_dx.sety(y)


def piastra_dx_giu():
    y = piastra_dx.ycor()
    y += -20
    piastra_dx.sety(y)


def salta():
    piastra_sx.goto(0, 0)


wn.listen()
turtle.onkeypress(piastra_sx_su, "w")
turtle.onkeypress(piastra_sx_giu, "s")
turtle.onkeypress(piastra_dx_su, "Up")
turtle.onkeypress(piastra_dx_giu, "Down")
turtle.onkeypress(salta, "r")


while True:
    #piastra_sx.forward(1)
    ball.forward(1)
    wn.update()
