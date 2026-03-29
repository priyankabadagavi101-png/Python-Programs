i=1
while i<=5:
    print(i)
    i=i+1

#WAP to sum of natural number from 1 to 10 using while loop
sum=0
i=1
while i<=10:
    sum=sum+i
    i=i+1
print("sum=",sum)

#WAP to print the count of even and odd from 1 to 10 using while loop
even=0
odd=0
i=1
while i<=11:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i+1
print("Even=",even)
print("Odd=",odd)

#zip() function is used to keep multiple rage function
for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i," ",j)

mul=1
i=1
while i<=5:
    mul=mul*i
    i=i+1
print("mul=",mul)

username=" " 
password=0
while username !="admin" or password !=12345:
    username=input("Enter username:")
    password=int(input("Enter password:"))

#Nested for loop
i= , j=
(i,j)=( , )
for i in range(1,4): #outer loop==>Row's
    for j in range(1,4): #inner loop==>Col's
        print(i,end=" ",)
    print()


#che() function convert the integer value in character ASCII
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1, n+1):
        print(chr(64+i),end=" ")
    print()


#WAP to find second largest element
list=[5,3,6,7,8,9]
list.sort()
print(list)
print(list[-2])

list=[5,0,5,3,0,1,2]
for i in list:
    if i==0:
        list.remove(i)
        list.append(i)
print(list)
