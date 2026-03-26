#.format
# print('Subjects Marks :')

phy = 50
chem = 60
math = 70

print("physics ={}  chemistry={}  Math={} ".format(phy, chem, math))
print("physics ={0}  chemistry={1}  Math={2} ".format(phy, chem, math))
print("physics ={x}  chemistry={y}  Math={z} ".format(x=phy, y=chem, z=math))

total = phy + chem + math

print("Total Marks", f"{total}")
print("Ro5ll No=", "7".zfill(4))

#Addition of two values
print(2+2)#4
print("2"+"2")#22
val1=int(input("Enter first number:"))
val2=int(input("Enetr second number:"))
print(val1+val2)

#bool()is used to convert
print(bool(0))
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(1+2j))
print(bool(0+0j))
print(bool(-1))
print(bool(False))
print(bool(True))
print(bool(" "))

#case(lower upper)
s= "Python is a high level programming language"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

#WAP to accept three paper marks and calculate total,percentage and if percentage is greater then egual to 60 he/she is eligible for placement else not eligible.
math=60
chem=70
phy=60
total=math+chem+phypercentagae=total/3.0
print("Total=",percentage)
if percentage >=60:
    print("you are eligible for placement")
else:
    print("you sre not eligible")

# int()used to convert
print(int(3.14))
print(int(10+j5))
print(int(True))#=1
print(int(False))#=0
print(int("4.22"))
print(int("4"))

# float()used to convert
print(float(3.14))
print(float(10+5j))
print(float(True))#1.0
print(float(False))#0.0
print(float("4.22"))#4.22
print(float("4"))

# bool()is used to convert
print(bool(0))
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(1+2j))
print(bool(0+0j))
print(bool(-1))
print(bool(False))
print(bool(True))
print(bool(" "))

# find()function return the starting index of given string and if string is not present then it returns default value-1
s="help4code is a best platform for practicing programming"
print(s.find("help4code"))
print(s.find("python"))
print(s.find("programming"))

#Height
Height=5
inch=Height*12
cm=inch*2.54
print("inch=",inch)
print("centimeter=",cm)

#Indexing
name=   "priyankabadagavi"
#indexing=012345678910
print(name[0])
print(name[1])
print(name[-1])
#print(name[15])Error string index out of range
print(name[0:5])
print(name[1:])
print(name[:5])
print(name[:])
print(name[1:9:2])
print(name[::-1])

#WAP to accept three paper marks and calculate total,percentage and if percentage is greater then egual to 60 he/she is eligible for placement else not eligible.
math=60
chem=70
phy=60
total=math+chem+phy
percentage=total/3.0
print("Total=",percentage)
if percentage >=60:
    print("you are eligible for placement")
else:
    print("you sre not eligible")

#simple interset
principal=100000
roi=10
time=1
si=principal*roi*time/100
print("simple interset=",si)

#conditional statement 
#simple if
#WAPto accept one single digit and check the entered number is positive, negative, zero.
N=int(input("Enter single digit:"))
if N>0:
    print("Entered number is positive")
if N<0:
    print("Negative number")
if N==0:
    print("Zero")

#WAP to accept days and check the working day or weekend
day =input("Enter Day:")
if day == "Saturday" or day == "sunday" or day == 'SATURDAY' or day =='sunday':
    print("Weekend")
else:
    print("Working day")


#1. rstrip() ==> To remove spaces at right hand side
#2. lstrip() ==> To remove spaces at left hand side
#3. strip()  ==> To remove spaces both sides

programming = input("Enter your programming Name: ")
p_name = programming.strip()

if p_name == "Python":
    print(p_name)

elif p_name == "Java":
    print(p_name)

elif p_name == "Cpp":
    print(p_name)

else:
    print("Wrong programming name")

#BODMAS
a=50
b=30
c=20
d=10
print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)

#WAP for swapping using third variable

val1=100
val2=200
print("Before Swapping",val1," ",val2)
temp=val1#temp=100
val1=temp#val2=200
val2=temp#val2=100
print("After Swapping",val1," ",val2)