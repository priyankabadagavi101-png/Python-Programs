#for (initialization; condition; inc/dec)

for i in range(1,11):#i=1
    print(i*2," ",i*3," ",i*4," ",i*5)#1 2 3 4
for i in range(1,11):
    print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)

#for(initialization; condition; inc/dec)
#WAP to print even and odd numbers
for i in range(1,11):
    if i%2==0:
        print("even=",i)
    else:
        print("odd=",i)

#WAP to print the count of even and odd numbers
even=0
odd=0
for i in range(1,11):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even=",even)
print("odd=",odd)

username=input("Enter Username:")
password=input("Enter Password")
if username==password:
    print("login successful")
else:
    print("Invalid login")

brand=input("Enter your cooldrink name either in upper case or in lower case but not combine:")
if brand =="pepsi"or brand=="PEPSI":
    print("swag")
elif brand=="dew"or brand=="DEW":
    print("dar ke age jeet hai")
elif brand=='thumsup'or brand=='THUMSUP':
    print('taste the thunder')
else:
    print('go with your brand')


n1=int(input("Enter first Number:"))
n2=int(input("Enter second Number:"))
n3=int(input("Enter third Number:"))
if n1>n2 and n1>n3:
    print("Biggest Number is:",n1)
elif n2>n3:
    print("Biggest Number is:",n2)
else:
    print("Biggeswt Number is:",n3)

n1=int(input("Enter first Number:"))
n2=int(input("Enter second Number:"))
n3=int(input("Enter third Number:"))
if n1<n2 and n1<n3:
    print("Smallest Number is:",n1)
elif n2<n3:
    print("Smallest Number is:",n2)
else:
    print("Smallest Number is:",n3)

mylist=["prashant","ashish","komal","ankush","ashish",77,"sandip",60.50,"prashant"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[1:8:2])
print(mylist[:])
print(mylist[::-1])

mylist[2]="akshay"
print(mylist)
# how to change the index value

if "ankush" in mylist:
    print("yes ankush is available")
else:
    print("not available")

mylist.append('harsh')
mylist.append("laxman")
print(mylist)

mylist.insert(1,"sanket")
print(mylist)
#if we have to add the value at specified index

mylist.remove("sandip")
print(mylist)

newlist=mylist.copy() #cloning
print(mylist)
print(newlist)

mylist=[['prashant','jha'],['85.56'],[440022,"yyy"]]
print("example of multidimentional list:")
print(mylist)
print(mylist[row][col])
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])

list1=["prashant","jha"]
print(list1*2)#it will print two times

list2=[50,25.50]
print(list1+list2)

list2=[50,25.50,'prashant']
del list2[2]
del list2
print(list2)

list2=[50,25.50,'prashant']
list2.clear()
print(list2)#[]

name="prashant"#str
print(name)
myname=list(name)#typecasting
print(myname)
#we have used list constructor

mylist=[40,30,20,10]
mylist.reverse()
print(mylist)

#sorting example
mylist=[44,53,0,53,88]
mylist.sort(reverse=True)
print(mylist)
#default sorting order for number is ascending order
#default sorting order for starting is alphabetical order
# we should know thet list should contain homogenious 
# data otherwise we will get TypeErrorpython2 first short number then string follow

mylist=[44,53,0,53,88]
newlist=mylist
print(id(mylist))
print(id(newlist))