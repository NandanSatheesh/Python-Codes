class Example:
    """This is a doc string"""

    x = 1
    y = 1
    print(x,y)

    def __init__(self):
        x = 10
        y = 10
        print(x,y)


    def print1(self):
        print("This is a print function")


ob = Example()

print(ob.print1())

print(ob.__doc__)