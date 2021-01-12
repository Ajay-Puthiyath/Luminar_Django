students=[[1001,"ajay","Engineering",150],
          [1007,"jay","MCA",149],
          [1002,"Vijay","MCA",145],
          [1001,"Sachin","Engineering",130],
          [1001,"Denny","Engineering",120],
          [1001,"Hardy","Engineering",110]]
#print(student)
for student in students:
    print(student[1])
for student in students:
    print(student[0])
    for student in students:
        if student[2]=="MCA":
            print(student)
    for student in students:
        if student[3]<140:
            print(student)
    totalmca=0
    totaleng=0
    for student in students:
        if student[2]=="MCA":
            totalmca+=student[3]
        elif student[2]=="Engineering":
            totaleng+=student[3]
    print("MCA total = ",totalmca)
    print("Engineering total = ",totaleng)

