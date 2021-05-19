#class    :design pattern
#object real world entity
# references   : name that refers a memory location of an object

# class Person:
#     def print(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.genger=gender
#         print(self.name,self.age,self.genger)
# pe=Person()
# pe.print("Jain",23,"male")
# re=Person()
# re.print("Owais",22,"Male")

# class Vehicle:
#     def car(self,company,name,color):
#         self.company=company
#         self.name=name
#         self.color=color
#         print(self.company,self.name,self.color)
# a=Vehicle()
# a.car("Tata","Harrier","Black")


# class Student:
#     def person(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#     def work(self,webdeveloper):
#         self.webdeveloper=webdeveloper
#         print(self.name,self.age,self.id)
#         print(self.webdeveloper)
# a=Student()
# a.person("Bilal",23,1521)
# a.work("html,css,javascript")

#
# class Addition:
#     def sum(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(self.num1+self.num2)
#
#
#
# c=Addition()
# a=int(input("enter the first value"))
# b=int(input("enter the second value"))
#
# c.sum(a,b)

#
#
# class Power:
#     def raiseto(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print(self.num1**self.num2)
#
# c=Power()
# a=int(input("enter the first value"))
# b=int(input("enter the second value"))
# c.raiseto(a,b)

#
# class Employee:
#     def setvalue(self,name,age,id,designation,company):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.designation=designation
#         self.company=company
#     def printvalues(self):
#         print(self.name)
#         print(self.age)
#         print(self.id)
#         print(self.designation)
#         print(self.company)
#
# a=Employee()
# a.setvalue("jain",23,1551,"webdeveloper","wipro")
# a.printvalues()
#
# a1=Employee()
# a1.setvalue("owais",22,"1552","c++ expert","amazon")
# a1.printvalues()

#two types of variables
#static variables...related to class..class name
#instance variable...related to method


# class Student:
#     school="saintjoseph"
#     def setvalue(self,name,age,rollno,clss):
#         self.name=name
#         self.age=age
#         self.rollno=rollno
#         self.clss=clss
#
#     def printvalue(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)
#         print("Roll no : ", self.rollno)
#         print("Class : ",self.clss)
#         print("school name : ",Student.school)
#
# a=Student()
# a.setvalue("Jain",16,10,"tenth")
# a.printvalue()
#
# b=Student()
# b.setvalue("Zaid",16,40,"tenth")
# b.printvalue()

#
# class Bank:
#     bank_name="Federal Bank"
#     def cr_acc(self,name,address,age):
#         self.name=name
#         self.address=address
#         self.age=age
#         self.min_bal=5000
#         self.balance=self.min_bal
#         print("Name : ",self.name)
#         print("Address : ",self.address)
#         print("Age : ",self.age)
#
#     def deposit(self,amt):
#         self.amt=amt
#
#         self.balance+=self.amt
#         print("Your ",Bank.bank_name ," account has been credited with rupees ",self.amt)
#         print("Your total balance is rupees : ",self.balance)
#
#     def withdraw(self,amnt):
#         self.amnt=amnt
#         if self.amnt>self.balance:
#             print("Insufficient balance")
#         else:
#             print(self.amnt," rupees has been withdrawn")
#             self.balance-=self.amnt
#             print("Your current balance is: ",self.balance)
#
#
#
#
#
#
# x=Bank()
# x.cr_acc("Jain","Flat no-10",23)
# x.deposit(5000)
# x.withdraw(6500)


#constructor : to initialize instance variables
# constructor automatically invoke when creating object

# class Person:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def printval(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)
#         print("Gender : ",self.gender)
#
# a=Person("Jain",23,"Male")
#
# a.printval()

#
# class Employee:
#     company="Wipro"
#     def __init__(self,name,id,age,designation):
#         self.name=name
#         self.id=id
#         self.age=age
#         self.designation=designation
#         self.salary=125000
#     def printval(self):
#         print("Name : ",self.name)
#         print("Id : ",self.id)
#         print("Age : ",self.age)
#         print("Designation : ",self.designation)
#         print("Salary : ",self.salary)
#         print("Company name : ",Employee.company)
#
# a=Employee("Jain",1234,23,"Web Developer")
# a.printval()



# class Student:
#     def student(self,name,age,rollno,subj):
#         self.name=name
#         self.age=age
#         self.rollno=rollno
#         self.subj=subj
#     def print(self):
#         print("Name : ",self.name)
#         print("Age : ", self.age)
#         print("Roll no : ", self.rollno)
#         print("Subject : ", self.subj)
#
# a=Student()
# a.student("Jain Abraham",23,10,"Maths")
# a.print()


#
# class Labour:
#     def labour(self,name,address,age):
#         self.name=name
#         self.address=address
#         self.age=age
#     def work(self,salary,work,hours):
#         self.salary=salary
#         self.work=work
#         self.hours=hours
#         print("Name : ",self.name)
#         print("Address : ", self.address)
#         print("Age : ", self.age)
#         print("Salary : ", self.salary)
#         print("Work : ", self.work)
#         print("Hours : ", self.hours)
# a=Labour()
# a.labour("Jain","Flat no 10",23)
# a.work(10000,"cement",12)


# class Bank:
#     bank="Federal Bank"
#     def customer(self,name,age,accno):
#         self.name=name
#         self.age=age
#         self.accno=accno
#     def printval(self,acctype):
#         self.acctype=acctype
#         print("Name : ",self.name)
#         print("Age : ", self.age)
#         print("Account No : ", self.accno)
#         print("Account Type : ", self.acctype)
#         print("Bank Name : ",Bank.bank)
#
# a=Bank()
# a.customer("Jain Abraham",23,15930100086173)
# a.printval("Savings")



# class Labour:
#     def __init__(self,name,age,add):
#         self.name=name
#         self.age=age
#         self.add=add
#     def print(self):
#         print(self.name)
#         print(self.age)
#         print(self.add)
#
# a=Labour("Jain",23,"Flat no 10")
# a.print()



