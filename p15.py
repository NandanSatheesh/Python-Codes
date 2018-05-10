import re

fhand = open("mbox-short.txt")

for line in fhand:
    line = line.rstrip()
    # print(line)
    l1 = re.findall("^Details:.*rev=([0-9.]+)",line)
    if( len(l1) > 0):
        print(l1)

