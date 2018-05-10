#

fhand = open("23.txt")

mainlist = []
for line in fhand:
    linelist = line.split()

    for word in linelist:
        if(word in mainlist):
            continue
        else:
            mainlist.append(word)

print("\n\n")
print(mainlist)