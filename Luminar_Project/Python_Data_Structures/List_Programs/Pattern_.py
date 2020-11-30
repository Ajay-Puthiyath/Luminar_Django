list = [6,6,8,9,4,2,3]
out = []
for num in list:
    if(num>5):
        num=num+1
        out.append(num)
    else:
        out.append(num-1)
print(out)