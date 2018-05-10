

fhandle = open("11.txt")
count = 0 ;

for line in fhandle:
    rpos = line.find('Received:')
    substr = line[rpos+len('received:'): line.find(' ',rpos)]
    print(substr)



