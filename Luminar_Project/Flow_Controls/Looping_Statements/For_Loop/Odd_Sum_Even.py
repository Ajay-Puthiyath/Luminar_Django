lower = int(input("Enter the lower limit"))
upper = int(input("Enter the upper limit"))
i = 0
evensum = 0
oddsum = 0
for i in range (lower,upper):
    if (i%2==0) :
        evensum = i + i
    i+=1
    print(evensum)
    if (i%2!=0):
        oddsum = i + i
    i +=1
    print(oddsum)

