
import math

class Circle:

    def __init__(self,radius =  0 ):
        self.__radius = radius

    def __str__(self):
        return 'this is a circle object '+str(self.__radius)

c1 = Circle()

print(c1)
