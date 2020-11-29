num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
if(num1<num2):
    print("The second number has the maximum value")
elif(num2<num1):
    print("The first number has the maximum value")
else:
    print("The two numbers share same value")