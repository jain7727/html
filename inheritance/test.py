# class Vehicle:
#     def vehicle(self,company,color,modelno):
#         self.company=company
#         self.color=color
#         self.modelno=modelno
#
# class Bus(Vehicle):
#     def bus(self,range,type,mileage):
#         self.range=range
#         self.type=type
#         self.mileage=mileage
#         print("Comapny : ", self.company)
#         print("Color : ", self.color)
#         print("Model no : ", self.modelno)
#         print("Range : ", self.range)
#         print("Type : ", self.type)
#         print("Mileage : ", self.mileage)
#
# a=Bus()
# a.vehicle("Benz","White",1234)
# a.bus("420kms","diesel","10kms\l")


#
# class Person:
#     def person(self,pname,page):
#         self.pname=pname
#         self.page=page
#         print(self.pname,self.page)
#
# class Child(Person):
#     def child(self,cname,cage):
#         self.cname=cname
#         self.cage=cage
#         print(self.cname,self.cage)
#
# class Subchild(Child,Person):
#     def subchild(self,sname,sage):
#         self.sname=sname
#         self.sage=sage
#         print(self.sname,self.sage)
#
#
#
# a=Subchild()
# a.subchild("abc",10)
# a.child("xyz",20)
# a.person("ABC",20)

#
# class Book:
#     Library_name="The American Library Association"
#     def book(self,book_name,author,pages):
#         self.book_name=book_name
#         self.author=author
#         self.pages=pages
#
#     def printbook(self):
#         print("Book name : ",self.book_name)
#         print("Author : ",self.author)
#         print("Pages : ",self.pages)
#         print("Library : ",Book.Library_name)
#
# a=Book()
# a.book(" Harry Potter and the Chamber of Secrets","J. K. Rowling",360)
# a.printbook()

#
# class Animal:
#     def __init__(self,type):
#         self.type=type
#         print("Type : ",self.type)
#
#     def dog(self,breed,name,age,color,status):
#         self.breed=breed
#         self.name=name
#         self.age=age
#         self.color=color
#         self.status=status
#         print("Breed : ",self.breed)
#         print("Name : ", self.name)
#         print("Age : ", self.age)
#         print("Color : ", self.color)
#         print("Status : ", self.status)
#
# a=Animal("Domestic")
# a.dog("Irish Setter","Judy",12,"Golden Brown","Dead")


#overriding is a method where we can use two or more than two same variables to initialize a program


# class Book:
#     def book(self,bname):
#         self.bname=bname
#         print("Name : ",self.bname)
#
#     def book1(self,bname):
#         self.bname=bname
#         print("Name : ",self.bname)
#
# class Book1(Book):
#     def book2(self,bname):
#         self.bname=bname
#         print("Name : ",self.bname)
#
# a=Book1()
# a.book1("Tom Jones")
# a.book2("Emma")


#
# class Student:
#     def student(self,name,rollno,stream,marks):
#         self.name=name
#         self.rollno=rollno
#         self.stream=stream
#         self.marks=marks
#     def printstudent(self):
#         print(self.name,self.rollno,self.stream)
#
# f=open("test1","r")
# for i in f:
#     d=(i.rstrip("\n").split(","))
#     # print(d)
#     name=d[0]
#     rollno=d[1]
#     stream=d[2]
#     marks=d[3]
#     a=Student()
#     a.student(name,rollno,stream,marks)
#     for i in marks:
#
#



# import re
# x="^a+[a-zA-Z0-9]*b$"
# a=input("enter the input")
# match=re.fullmatch(x,a)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")


# import re
# x="[A-Z]+[a-z]*$"
# a=input("enter the input")
# match=re.fullmatch(x,a)
# if match is not None:
#     print("Match found")
# else:
#     print("Match not found")







# import re
# f=open("file2","r")
# x = "[0-9]{12}"
# for i in f:
#     i=i.rstrip("\n")
#     match = re.fullmatch(x, i)
#     if match is not None:
#         print("valid")
#     else:
#         print("not valid")











