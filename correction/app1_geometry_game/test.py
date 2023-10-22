import turtle

from random import randint


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


myturtle = turtle.Turtle()


myturtle = turtle.Turtle()


class GraphicalRectangle(Rectangle):

    def draw(self, canvas=myturtle):
        canvas.penup()
        # Le point (0,0) c'est le centre du canves
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()

        largeur = self.point2.x - self.point1.x
        hauteur = self.point2.y - self.point1.y
        # Dessin d'un rectangle
        canvas.forward(largeur)
        canvas.left(90)
        canvas.forward(hauteur)
        canvas.left(90)
        canvas.forward(largeur)
        canvas.left(90)
        canvas.forward(hauteur)

        turtle.done()


point2 = Point(10, 10)
point1 = Point(50, 60)
rectangle = GraphicalRectangle(point1, point2)
rectangle.draw()
