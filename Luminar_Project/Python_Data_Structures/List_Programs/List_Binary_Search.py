list = [2,1,5,8,7,6,8,10,3,11]
for i in range(0,len(list)):
    for j in range ((i+1),len(list)-1):
        if(list[i]>list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)
list = [2,1,5,8,7,6,8,10,3,11]
element = int(input("Enter the element : "))
for i in range(0,len(list)):
    for j in range ((i+1),len(list)):
        if(list[i]<list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)
#Sorting done
#now binary search
low = 0
upp = len(list)-1
flag = 0
#print(upp)
while(low<upp):
    mid = (low + upp)//2
    if(element>list[mid]):
        low=mid+1
    elif(element<list[mid]):
        upp=mid-1
    elif(element==list[mid]):
        flag = 1
        break
if(flag>0):
    print("Element found")
else:
    print("Element not found")

#print(mid)
