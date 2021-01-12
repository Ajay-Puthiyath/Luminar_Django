employee=[[1001,"ajay","Engineer",150000],
          [1007,"jay","Devops",149000],
          [1002,"Vijay","Devops",145000],
          [1001,"Sachin","Engineer",130000],
          [1001,"Denny","Engineer",120000],
          [1001,"Hardy","Engineer",110000]]
totalsal=0
totaldevo=0
totaleng=0
#Print all employee id
for emp in employee:
    print(emp[0])
#Find total of salary
for emp in employee:
    totalsal += emp[3]
    print(totalsal)
#Find how many members working as devops
#Find total salary group by designation
for emp in employee:
    if(employee[2]=="Devops"):
        totaldevo+=employee[3]
#Print all designation
#print all emp des is devops
#print all employee those who are working in 1980's add year
#print all employee detais whose experience less than 9 yeras
