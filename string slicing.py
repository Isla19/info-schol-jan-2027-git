name="Manujana"
print(name)
#man print
print(name[0:4])

#need to print "jana"
print(name[4:8])
#need to print "Mnjn"
print(name[0:8:2])

name="alphabet"
print(name[1:9:3])

fruit="Orange"
#print first three characters
print(fruit[0:3])
#print last three characters
print(fruit[3:7])

fruits=["Orange","Apple","Banana",1,2,3,True,"Apple"]
print(fruits)
print(fruits[:3])
print(fruits[5:8])

fruits[1]="Banana"
print(fruits)

fruits.insert(3,"Grapes")
print(fruits)

#append
fruits.append("False")
print(fruits)

#remove
fruits.remove("Banana")
print(fruits)

#pop
fruits.pop(7)
print(fruits)

#delete
del fruits[5]
print(fruits)

#clear
fruits.clear()
print(fruits)

names = "jasmine", "sunny","lilac","kalif","sabrina"
print(names)

#list down vertically
for x in names:
    print(x)

#list down horizontally
for x in names:
    print(x, end="")
    print(x, end=" ")
    print(x, end=",")


name = "Rukman"
print(name)

#uppercase
Uppername = name.upper()
print(Uppername)

#lowercase
Lowername = name.lower()
print(Lowername)