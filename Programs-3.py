#Tuple
mytuple=("prashant","ashish","rahul","sandip","komal","ankush","rajesh",23,35.24,77,"sandip")
print(mytuple)
print(type(mytuple))
print(mytuple[2])

mytuple[2]="sunil"
print(mytuple)

#Set Datatype
myset={1,2,"sanjay",5.66,"rahul","ayush","rajesh","ankit","rishikesh"}
print(myset)
print(type(myset))

myset.add(60)
print(myset)

myset.discard(3)
print(myset)

myset.remove(3)
print(myset)

#Union()
myset={10,20,30,40}
yourset={"prashant","jha"}
newset=myset.union(yourset)
print(newset)

#Intersection return common element
myset={10,20,30,40}
yourset={10,50,60,30}
print(myset.intersection(yourset))

#Difference() methodthis will return the element
#present in first set but not in second set
myset={10,20,30,40}
yourset={10,50,60,30}
print(myset.difference(yourset))

# Clear() we can use to clear data
# pop() method is used to remove object
myset={10,20,30,40}
print(myset.pop())
print(myset.clear())

#dict Datatype
#Indexing and slicing is not possible in dictionary()
mydict={
    "name":"prashant",
    "professional":"developer",
    "empid":1001 
}
print(mydict)
print(type(mydict))

mydict={
    101:"prashant",#101 is previous saved data
    102:"ashish",
    "103":"mohini",
    "104":"triveni",
    101:"ashish",#101 will print 'ashish' because data will be update
    104:"ashish",#104 will print two time because of both are different those are string & intiger
}
print(mydict)

#with the help of key we have to print values
a=mydict[102]
print(a)

#We will replacce old valu by new value
mydict[102]="peter"
print(mydict)

#only print key x=0,1
for x in mydict:
    print(x)

#only print values x=0
for x in mydict.values():
    print(x)

#printing key and values both
for x,y in mydict.items():
    print(x,y)

# if I have to add key and value pair in my dictionary
mydict["mobil_no"]=2583691472
print(mydict)

#pop() method remove pair by specific key name
mydict={
    "name":"prashant",
    "professional":"developer",
    "empid":1001 
}
mydict.pop("name")
print(mydict)

newdict=mydict.copy()
print(newdict)

#Loop
for i in range(1,5):
    if i==6:
        break
    print(i)

for i in range(1,5):
    if i==4:
        continue
    print(i)

list=[10,20,30,40,50]
for i in list:
    print(i)

mycart=[10,20,200,300,800,60,700]
for i in mycart:
    if i>400:
        print("This is my purchased cart item")
        continue
    print(i)

# WAP to calculate the sum of list elements
list=[1,2,3,4,5,6,7,8,9,10]
sum=0
for x in list:
    sum=sum+x
print("The Sum=",sum)

# Indexing
name="prashant"
newname=""
for i in name:
    if i not in newname:
        newname +=i 
print(newname)

rollno=[3,5,7,1,11,4,5,2]
for x in rollno:
    if x==2 or x==4 or x==6 or x==8 or x==10:
        print("even no is found",x)
        break

# s.replace(oldstring,newstring)
# inside s, every occarrence of oldstring will be replaced with newstring.
s=" "
s1=s.replace("difficult","easy")
print(s1)
#All occurrences will be replaced
s="abababababababab"
s1=s.replace("a","b")
print(s1)

x=['A','B','C']
y=['A','B','C']
z=[1,2,3,4]
print(x==y)
print(x==z)
print(x !=z)

val=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(val.index(1))
print(val.index(2))
print(val.index(3))
print(val.index(4))
print(val.index(5))
print(val.index(6))
# index returning the index value

n=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))
print(n.count(5))
print(n.count(6))
print(n.count(7))
# count is returning the index repeated times

import datetime 
# datetime formatting
date=datetime.datetime.now()
print("It's now:{:%d/%m/%Y %H:%M:%S}".format(date))