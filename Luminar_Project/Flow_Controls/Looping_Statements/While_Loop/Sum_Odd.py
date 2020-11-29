lower = int(input("Enter the lower limit "))
upper = int(input("Enter the upper limit "))
i = lower
sum = 0
if(lower>upper):
    while(lower<upper):
        if(lower%upper!=0):
            sum+=lower
            lower+=1
    print(sum)