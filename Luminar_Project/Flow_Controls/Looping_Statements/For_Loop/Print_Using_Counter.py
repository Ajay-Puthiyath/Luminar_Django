cnt = 1
for i in range (1,13):
    print(i, end = "\t")
    if(cnt==4):
        print()
        cnt=1
    else:
        cnt+=1
