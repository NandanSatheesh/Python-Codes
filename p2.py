

total = 0
count = 0
while True:
    try:
        n = input("enter a number. enter done to exit\n")
        if(n=="done"):
            break
        else:
            total += int(n)
            count+=1
    except:
        print("input error. enter an integer only\n")


average = total/count
print(total , count , average)
