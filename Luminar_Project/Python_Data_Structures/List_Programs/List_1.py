name=[]
print(type(name))

#OR

name=list()
print(type(name))

#OR

name = ["java","python","C#", "javascript"]
print(name)

#Indexing
print(name[0])
print(name[2])
print(name[-1])
print(name[-1:-5:-1])
print(name[:3])
#[Lower:Upper]
print(name[0:4:2])

#Iteration

for item in name:
    print(item)
# Adding new element

name.append("dark")
print(name)

#updating list

name[0]= "ruby"
print(name)

#duplicate value can be store
name = ["java","python","C#", "javascript","java","python","C#", "javascript"]
print(name)

#insert an element in between
name.insert(3,"perl")
print(name)