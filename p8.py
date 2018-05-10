def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

ch = input("Enter choice :")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if ch == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif ch == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif ch == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif ch == '4':
    if(num2==0):
        print("Divide by Zero Error!")
    else:
        sprint(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")