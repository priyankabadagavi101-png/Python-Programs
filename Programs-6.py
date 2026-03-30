class student: #first character of classname must be capital
    roll_number=101
    num1=50
    num2=100  #data member #2byte

    def add(self):#member function
        print(self.num1+self.num2)
        self.name=input("Enter name:")  #name is your new type of variable
        print(self.name)
    
    #-----------------------------------------
obj=student() #object create outside a class
obj.add()  #calling function
print(obj.roll_number) 


#Constructor
# By using the constructor we initialize the object
#constructor call automatically whenever we create object or we can say that the time of creatin of object

class NewClass:
    def __init__(self):   # constructor declaration (called automatically)
        print("constructor always execute first")

    def show(self):   # member function inside class
        print("welcome to class level programming")


obj = NewClass()   # creating an object
# print(obj)
obj.show()

obj1 = NewClass()


class Hod:
    def __init__(self):  #constructor
        self.name="prashant jha"  #2byte
        self.age=53               #3byte
        self.empid=1001           #1byte

    def info(self):
        print("My name is:",self.name)
        print("My age is:",self.age)
        print("My emp id is:",self.empid)
obj=Hod()#object create
obj.info()


class Hod:
    def __init__(self,name,age,rollno):  # parameterizeconstructor
        self.age=53               
        self.rollno = rollno #parameterize constuctor   
        self.name=name       

    def show(self):
        print('name=',self.name)
        print('age=',self.age)
        print('rollno=',self.rollno)
obj=Hod('Arjun',45,101)#object create
obj.show()

#how many types of variable we declere inside the class
#==>three types
#1. class method
#2. Instance variable
#3. Static variable  #one static variable=one memory
    #Instance method==> If any instance variable we are implementing inside of any method then rthat method we will be calledinstance method


class New:
    def __init__(self):
        self.a= 10

obj1 =New()
obj2 =New()
obj3 =New()
print(obj1.a)
print(obj2.a)
print(obj3.a)
obj2.a=20
print(obj1.a)
print(obj2.a)
print(obj3.a)

#How to access static variable? There are two ways to access the static variable the first one is by class name or
#  second way is by onject but programmer recommended to access by class name
#By using obje or self variable we can access or read static variable but we can not do modification or deletion
#If we try to delete them we will get error

class New:
    a=10 #static variable

    def __init__(self):
        self.name="Priyanka"

obj1 =New()
obj2 =New()
obj3 =New()
print(obj1.a)
print(obj2.a)
print(obj3.a)
New.a=50
print(obj1.a)
print(obj2.a)
print(obj3.a)

#Instance method==> If any instance variable we are implementing inside of any method then rthat method we will be calledinstance method

class Student:
    def __init__(self,name,rollno,mob):  # parameterizeconstructor
        self.name=name              
        self.rollno = rollno #parameterize constuctor   
        self.mob=mob       

    def display(self):
        print(self.name," ",self.rollno," ",self.mob)
       
stud=Student('Prashant',1001,646464646464)#object create
stud.display()


class Student:
    # by using class name we can access static method

    @staticmethod  # decorator
    def get_personal_detail(firstname, lastname):
        print("your personal detail=", firstname, lastname)

    @staticmethod
    def contact_detail(mobil_no, rollno):
        print("your contact detail=", mobil_no, rollno)


Student.get_personal_detail("Priyanka", "Badagavi")
Student.contact_detail(5456454646, 1001)
