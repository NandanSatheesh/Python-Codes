#

fhandle = open("23.txt")

d = dict()

for line in fhandle:
    line = line.strip()

    words = line.split()

    for word in words:
        if(word not in d):
            d[word] = 1
        else:
            d[word] += 1


print("\n\n")
print(d)
