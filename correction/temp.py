class House:
    def __init__(self, wall_area):
        self.wall_area = wall_area


class Paint:
    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def prix_total(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19


paint1 = Paint(5, "red")
print(paint1.prix_total())
