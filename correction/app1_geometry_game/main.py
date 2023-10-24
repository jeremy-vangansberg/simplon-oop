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

    def distance_from_point(self, point):
        x = point.x
        y = point.y
        return ((self.x - x)**2 + (self.y - y)**2)**(1/2)


class Rectangle:

    def __init__(self, point1, point2):
        # On s'assure que point1 est en bas à gauche
        # et que point2 est en haut à droite
        self.point1 = Point(min(point1.x, point2.x), min(point1.y, point2.y))
        self.point2 = Point(max(point1.x, point2.x), max(point1.y, point2.y))

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


# Create rectangle object
rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                      Point(randint(10, 19), randint(10, 19)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ",
      user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)
