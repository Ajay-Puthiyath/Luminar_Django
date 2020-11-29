num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if(num1>=num2) and (num1>=num3):
    largest = num1
    print("The largest number is",largest)
elif(num2>=num1) and (num2>=num3):
    largest = num2
    print("The largest number is",largest)
else:
    largest = num3
    print("The largest number is",largest)
if(num1>=num2) and  (num1<=num3) or (num1>=num3) and (num1<=num2):
    secondLargest = num1
    print("the second largest number is", secondLargest)
if (num2 >= num1) and (num2 <= num3) or (num2 >= num3) and (num2 <= num1):
    secondLargest = num2
    print("the second largest number is", secondLargest)
if (num3 >= num2) and (num3 <= num1) or (num3 >= num1) and (num3 <= num2):
    secondLargest = num3
    print("the second largest number is", secondLargest)
a1 = min(num1,num2,num3)
a3 = max(num1,num2,num3)
a2 = (num1+num2+num3) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)
