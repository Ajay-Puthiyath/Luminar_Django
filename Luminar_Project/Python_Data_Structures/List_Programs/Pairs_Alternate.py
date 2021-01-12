list =[1,8,5,2,3,6,9,7,4,1]
list.sort()
low = 0
upp = len(list)-1
#print(list)
element = int(input("Enter the element "))
while(low<upp):
    total = list[low]+list[upp]
    if(element<total):
        upp=upp-1
    elif(element>total):
        low=low+1
    elif(element==total):
        print("The pairs are", list[low],"",list[upp])
        break