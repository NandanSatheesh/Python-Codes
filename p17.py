import math

class Point:
    x = 0
    y = 0
    def __init__(self,a,b):
        x = a
        y = b

    def distance_between_points(self,a,b):
        print(a.x , a.y)
        print(b.x , b.y)
        print(math.sqrt((a.x-b.x)**2 - (a.y-b.y)**2))


a = Point(3,4)

b = Point(0,0)

print(a.distance_between_points(a,b))