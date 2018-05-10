import datetime

class Time:
    """Consists of 3 attributes"""

    def __init__(self,hour = 0 , min = 0 , sec  = 0 ):
        self.hour = hour
        self.min = min
        self.sec = sec


    def print_time(Time):
        print("%.2d:%.2d:%.2d"%(Time.hour,Time.min,Time.sec))

t1 = Time(10,10,10)

Time.print_time(t1)

l1 = str(datetime.datetime.now()).strip()

print(l1)

