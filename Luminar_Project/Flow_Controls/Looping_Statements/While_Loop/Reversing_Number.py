number = input("Enter the number : ")
i =1
sum = 0
while (i<=int(number)):
    #print((number*i))
    data = number * i
    sum = sum + int(data)
    i+=1
    print(sum)