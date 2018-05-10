import random
import math



largest = None

smallest= None



n = int(input("enter the number of elements"))


str1 = "test"
for i in range(0,n,1):
    str1 += "," + str(random.randint(0,1000))


print(str1)

#a = [int(x) for x in input().split()]


str2 = input("enter the values for the list").
l1 = str1.split(",")
l1 = l1[1:]

for x in l1:
    if largest == None or x> largest:
        largest = x

    if smallest == None or x<smallest:
        smallest=x

    print("loop largest ",x,largest)
    print("loop smallest", x, smallest)

print("largest",largest,"smallest",smallest)
