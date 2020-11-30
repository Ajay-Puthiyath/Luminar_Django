limit = int(input("Enter the limit "))
list = list()
for i in range (1,(limit+1)):
    list.append(i)
print(list)
even = []
odd =  []
for num in list:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(odd)
print(even)