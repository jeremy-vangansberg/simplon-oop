class Point:
    def __init__(self, x, y):
        print("Bonjour, je suis __init__ !")
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        print("Je suis une méthode normale !")
        # lowleft et upright sont les coordonnées du coin
        # en bas à gauche et en haut à droite du rectangle
        if lowleft[0] < self.x < upright[0]\
                and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def distance_from_point(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**(1/2)


point1 = Point(1, 1)
point1.distance_from_point(3, 3)


##
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        # lowleft et upright sont les coordonnées du coin
        # en bas à gauche et en haut à droite du rectangle
        if lowleft[0] < self.x < upright[0]\
                and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

    def distance_from_point(self, point):
        x = point.x
        y = point.y
        return ((self.x - x)**2 + (self.y - y)**2)**(1/2)


point1 = Point(1, 1)
point2 = Point(2, 2)

point1.distance_from_point(point2)
