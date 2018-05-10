
a = list()

while True:
    inp = input("enter the numbers for the list or enter done to quit\n")
    if(inp == 'done'): break

    a.append(int(inp))

print(a)
print(max(a))
print(min(a))
print(sum(a))
print(sum(a) / len(a))
print(len(a))

print(a.pop())
print(a)
print(a.pop())

#print(del(a[2]))
print(a)

#print(del(a[1]))
print(a)

