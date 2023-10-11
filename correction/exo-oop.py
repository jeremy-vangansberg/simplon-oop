
class House:  # 1

    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):   # 3
        return self.wall_area * 2.5


class Paint:  # 2

    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def total_price(self):   # 4
        if self.color == 'white':
            total = self.buckets * 1.99
        else:
            total = self.buckets * 2.19
        return total
