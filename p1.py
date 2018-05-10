
a = int(input(print("enter first numbers")))
b = int(input(print("enter the second number")))

print("the values before swapping are a = ",a," and b = ",b)

t = a
a = b
b = t


print("a = ",a)
print("b = ",b)


a,b = b,a

print("a = ",a)
print("b = ",b)