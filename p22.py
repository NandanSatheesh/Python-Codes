l1 = [0,1]

while(len(l1) <= 406):
    l1.append(l1[-1] + l1[-2])


print(l1[406])
print(str(l1[-1])[-10:])