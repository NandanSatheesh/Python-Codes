
c=0
fhand = open("11.txt")
for line in fhand:
    if line.startswith('From'):
        t=line.split()
        c+=1
        print(t[1])

print(c)