number = int(input("Enter the number"))
flag = 0
for i in range (2,number):
    if (number%i==0):
        flag = 1
        break
    else:
        flag = 0
    if (flag==0):
        print("The given number is prime")
    else:
        print("The given number is not a prime")
