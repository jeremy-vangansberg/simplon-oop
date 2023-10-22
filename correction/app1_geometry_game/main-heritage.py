from random import randint
import turtle


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
        # On s'assure que point1 est en bas à gauche
        # et que point2 est en haut à droite
        self.point1 = Point(min(point1.x, point2.x), min(point1.y, point2.y))
        self.point2 = Point(max(point1.x, point2.x), max(point1.y, point2.y))

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


# myturtle = turtle.Turtle()


class GraphicalRectangle(Rectangle):

    def draw(self, canvas):
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


class GraphicalPoint(Point):
    def draw(self, canvas, size=5):
        canvas.penup()
        # Le point (0,0) c'est le centre du canves
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size=size)


# Create rectangle object
rectangle = GraphicalRectangle(Point(randint(0, 400), randint(0, 400)),
                               Point(randint(10, 400), randint(10, 400)))


# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = GraphicalPoint(
    float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()
