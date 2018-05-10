class Time:

    def __init__(self):
        self.hr = 0
        self.min = 0
        self.sec = 0

    def __init__(self, sec, min, hr):
        self.hr = hr
        self.min = min
        self.sec = sec

    def showtime(self, t):
        print('the time is %d hrs %d min %d sec' % (t.hr, t.min, t.sec))

    def addtime(self, t1, t2):
        t2.sec += t1.sec
        t2.min += t1.min
        t2.hr += t1.hr

        if (t2.sec >= 60):
            t2.sec -= 60
            t2.min += 1

        if (t2.min >= 60):
            t2.min -= 60
            t2.hr += 1

        t2.showtime(t2)


ob = Time(59, 1, 1)

ob2 = Time(2, 59, 2)

ob.addtime(ob, ob2)



# It Changes one or more object it receives as arguments. Most of the modifiers are void. They return null.
# Invariants - can help to detect errors and find their process.
# Write the definition for a class name circle with attributes
# center and radius where center is a point object and radius is a number
# instantiate a circle with it's center at (150,100) and radius 75
# write a function named point_in_circle that takes a circle and a point
# and returns true if the point lies in or on the boundary of the circle.
# Write a function name rect_in_circle that takes a circle and a rectangle and returns true
# if the rectangle lies entirely in or on the boundary of the circle.

# use the datetime module to write a program that gets the current date and prints the day of the week.
#
#