import math
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
    def midpoint(p1 , p2):
        mx = (p1.x + p2.x) / 2
        my = (p1.y + p2.y) / 2
        p3 = Point(mx , my)
        return p3

p1 = Point(3,4)
p2 = Point(5,10)
p3 = p1.midpoint(p2)
print(p3.x , p3.y)
distance =p1.distance_from_origin()
print(distance)
