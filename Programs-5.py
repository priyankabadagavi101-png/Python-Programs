# def message(): #called function 
#     print("Hello world!")
# message() #calling function
# message()

# def login():
#     username = input("Enter your username:")  
#     password = input("Enter your password:")  
#     if username == password:  
#         print("login successfully")   
#     else:  
#         print("you have entered wrong credentials")  

# login()#calling function

# def add():
#     return 2+3

# print(add())

# def add():
#     return 2+3

# result=add()
# print("Result=",result)


#can a function return multiple value in python
# def add():
#     a=int(input("Enter value of a:"))
#     b=int(input("Enter value of b:"))
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add, sub, mul, div #it will return in Tuple
# print(add())

# def add():
    # a=int(input("Enter value of a:"))
    # b=int(input("Enter value of b:"))
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add, sub, mul, div #it will return in Tuple

# result=add()
# print("Result=",result)
# print(result)

# How many types of arguments we can pass in function 
# ==>there are 4 types of arguments we can pass in funcction
# 1.Positional argument
# 2.keyword argument
# 3.default argument
# 4. variable number of argument or variable length of argument

#Positional argument
# def name(a,b):
#     print(a+b)

# name(2,3)

# def personInfo(fname,lname):
#     print("First name=",fname)
#     print("Last name=",lname)

# personInfo("prashant","jha")

#keywaord argument
# def profile(fname,lname):
#     print("first name=",fname)
#     print("Last name=",lname)

# profile(fname="prashant",lname="jha")

#Default argument
# def cityName(city): #without argument
#     print("City Name=",city)

# cityName("Nagpur")
# cityName("Delhi")
# cityName()

# def cityName(city="Banglore"): #with argument
#     print("City Name=",city) 

# cityName("Nagpur")
# cityName("Delhi")
# cityName()

#variable number of arguments/variable length of arguments
# def city(*name):
#     print(name)
# city("Delhi", "Nagpur", "Mumbai", "Pune", "Banglore")

#WAP to do amenu friven program using arithmetic operation
# import sys
# def addition():
#     a=int(input("Enter value of a:"))
#     b=int(input("Enter value of b:"))
#     print("Addition=",a+b)

# def substraction():
#     a=int(input("Enter value of a:"))
#     b=int(input("Enter value of b:"))
#     print("substraction=",a-b)

# def Multiplication():
#     a=int(input("Enter value of a:"))
#     b=int(input("Enter value of b:"))
#     print("Multiplication=",a*b)

# def Division():
#     a=int(input("Enter value of a:"))
#     b=int(input("Enter value of b:"))
#     print("Division=",a/b)

# while True:
#     print("1. Addition")
#     print("2. substraction") 
#     print("3. Multiplicaton")
#     print("4. Division")
#     print("5. Exit")
#     choice=(int(input("Enter your choice:")))
#     if choice==1:
#         addition()
#     elif choice==2:
#         substraction()
#     elif choice==3:
#         Multiplication()
#     elif choice==4:
#         Division()
#     elif choice==5:
#         sys.exit()

#Calculate factorial
# # def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# num=int(input("Enter a number:"))
# result=fact(num)
# print("Factorial of",num,"is",result)

##Check primre number
# import math

# def is_prime(n):
#     if n <= 1:
#         return False   
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False   
#     return True
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(num, "is a Prime number")
# else:
#     print(num, "is NOT a Prime number") 
         

# try:
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("can't devide be zero")
# except ValueError:
#     print("Enter only integer value")

#Handling multiple different kinds of exception with 
#Single except block
# try:
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError)as message:
#     print(message)

#The concept of default except block, generally we used for
#Writing normal message or showing normal error
# try:
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError)as message:
#     print("Enter the correct number:", message)
# except:
#     print("Ths is default part of the except block")


# try:
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError)as message:
#     print("Enter the correct number:", message)
# except:
#     print("Ths is default part of the except block")
# else:
#     print("Everything is ok")


#Finally block will always executed whether try block generate error or not
# try:
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except (ValueError, ZeroDivisionError)as message:
#     print("Enter the correct number:", message)
# finally:
#     print("I will always executed")

#nested try except block
# try:
#     a=int(input("Enter first number:"))
#     b=int(input("Enter second number:"))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)


#user defined exception by raise keyword
bank_bal = 5500
if bank_bal < 2000:
    raise Exception("your account balance is below a accessing limit")
else:
    print("Your amount has withdrawal")