import turtle

# Défini un canvas
myturtle = turtle.Turtle()

myturtle.penup()
# Le point (0,0) c'est le centre du canves
myturtle.goto(10, 50)
myturtle.pendown()

# Dessin d'un rectangle
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)

# Permet de garder le résultat
turtle.done()
