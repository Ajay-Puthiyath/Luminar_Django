num1 = int(input())
num2 = int(input())
print(type(num1))
print("The values before swapping num1 = ",num1, "num2 = ",num2)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("The values after swapping num1 = ",num1, "and num2 = ",num2)