import re

fhand = open("mbox-short.txt")

for line in fhand:
    line = line.rstrip()
    # print(line)
    if(re.search("^X\S.*:[0-9.]+",line)):
        print(line)