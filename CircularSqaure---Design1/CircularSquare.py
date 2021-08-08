import turtle

akash = turtle.Turtle()
turtle.bgcolor("black")

akash.speed(100)
akash.pencolor('#ffffe6')
akash.pensize(0.2)

area = 0

while area < 430:
    akash.forward(2+area)
    akash.right(90.899)

    area = area + 1

turtle.done()