list = [1,2,3,4,5,6,7,8]
element = int(input("Enter the element for searching"))
if(element in list):
    print("Element found")
else:
    print("Element is not found")
#Or
list = [1,2,3,4,5]
element = int(input("Enter the element for searching"))
flag = 0
for num in list:
    if (num ==element):
        flag+=1
        break
    else:
        flag=0

if(flag>0):
    print("Element found")
else:
    print("Element not found")