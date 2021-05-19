#single inheritance      (child class can inherit parent class

# class Person:                # Parent/base/super class
#     def details(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def printdet(self):
#         print("Name : ",self.name)
#         print("Age : ", self.age)
#         print("Gender : ", self.gender)
#
# class Student(Person):         # child/sub/derived class
#     def det(self,rollno,school):
#         self.rollno=rollno
#         self.school=school
#     def print(self):
#         print("roll no : ",self.rollno)
#         print("School : ",self.school)
#
# a=Person()
# a.details("Jain",23,"Male")
# a.printdet()
#
# st=Student()
# st.det(10,"Saint joseph")
# st.print()
#
# st.details("Owais",22,"Male")
# st.printdet()

#
#
# class Person:
#     def details(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
#     def printdetails(self):
#         print("Name : ",self.name)
#         print("Id : ",self.id)
#         print("Age : ",self.age)
#
# class Employee(Person):
#     def det(self,salary,totalhrs,desig):
#         self.salary=salary
#         self.totalhrs=totalhrs
#         self.desig=desig
#     def printdet(self):
#         print("Salary : ",self.salary)
#         print("Total Hours / day : ",self.totalhrs)
#         print("Designation : ",self.desig)
#
# a=Person()
# a.details("Jain",1551,23)
# a.printdetails()
# b=Employee()
# b.det(15000,8,"Web development")
# b.printdet()
#
# b.details("Jibin",1552,23)
# b.printdetails()


# multiple inheritance    it can have multiple parent class

# class Parent:
#     def parent(self):
#         print("parent")
#
# class Child:
#     def child(self):
#         print("child")
#
# class Subchild(Child,Parent):
#     def subchild(self):
#         print("subchild")
#
# a=Subchild()
# a.subchild()
# a.parent()
# a.child()

#
# class Cars:
#     def cars(self,company,name):
#         self.company=company
#         self.name=name
#
#     def printcars(self):
#         print("Comapny : ",self.company)
#         print("Name : ",self.name)
#
# class Model:
#     def model(self,model_no,chasis_no):
#         self.model_no=model_no
#         self.chasis_no=chasis_no
#
#     def printmodel(self):
#         print("Model no is : ",self.model_no)
#         print("Chasis no is : ",self.chasis_no)
#
# class Price(Cars,Model):
#     def price(self,exshowroom,on_road):
#         self.exshowroom=exshowroom
#         self.on_road=on_road
#
#     def printprice(self):
#         print("Ex-showroom price : ",self.exshowroom)
#         print("On-road price : ",self.on_road)
#
# a=Price()
# a.cars("Volvo","X60")
# a.printcars()
# a.model(12345,327854832)
# a.printmodel()
# a.price(2500000,3000000)
# a.printprice()



#multilevel inheritance   dadaji pitaji beta

# class Parent:
#     def parent(self):
#         print("Parent")
#
# class Child(Parent):
#     def child(self):
#         print("Child")
#
# class Subchild(Child):
#     def subchild(self):
#         print("Subchild")
#
# a=Subchild()
# a.subchild()
# a.child()
# a.parent()

#
# class College:
#     def college(self,coll_name,loc):
#         self.coll_name=coll_name
#         self.loc=loc
#     def printcollege(self):
#         print("College name : ",self.coll_name)
#         print("Location : ",self.loc)
#
# class Dept(College):
#     def dept(self,dept_name,fees):
#         self.dept_name=dept_name
#         self.fees=fees
#
#     def printdept(self):
#         print("Department name : ",self.dept_name)
#         print("fees : ",self.fees)
#
# class Student(Dept):
#     def student(self,name,score,age):
#         self.name=name
#         self.score=score
#         self.age=age
#
#     def printstudent(self):
#         print("Name : ",self.name)
#         print("Score : ",self.score)
#         print("Age : ",self.age)
#
# a=Student()
# a.student("Jain",78,23)
# a.printstudent()
# a.dept("Information Science",76000)
# a.printdept()
# a.college("PDA college of Engg","Gulbarga")
# a.printcollege()

#
#
# class Person:
#     def person(self,name,age):
#         self.name=name
#         self.age=age
#     def printperson(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)
#
# class Child(Person):
#     def child(self,name,age):
#         self.name=name
#         self.age=age
#     def printchild(self):
#         print("Name : ",self.name)
#         print("Age : ",self.age)
#
# class Parent(Person):
#     def parent(self,salary,loc):
#         self.salary=salary
#         self.loc=loc
#     def printparent(self):
#         print("Salary : ",self.salary)
#         print("Location : ",self.loc)
#
# class Student(Child):
#     def student(self,name,id):
#         self.name=name
#         self.id=id
#     def printstudent(self):
#         print("Name : ",self.name)
#         print("Id : ",self.id)
#
# a=Parent()
# a.parent(10000,"flat no-0")
# a.printparent()
# b=Student()
# b.student("Owais",1551)
# b.printstudent()
#
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     # def print(self):
#     # print("Name : ", self.name)
#     # print(" Age : ", self.age)
#
#
# class Child(Person):
#     def __init__(self,school,rollno,name,age):
#         super().__init__(name,age)
#         self.school=school
#         self.rollno=rollno
#
#     def printval(self):
#         print("Name : ", self.name)
#         print(" Age : ", self.age)
#         print("School : ",self.school)
#         print("Roll no : ",self.rollno)
#
#
# a=Child("Saint joseph",10,"Jain",23)
# # a.print()
# a.printval()

#
# class Calculator:
#     def calci(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#
#     def calculate(self):
#         print("sum is",self.num1+self.num2)
#         print("pro is",self.num1*self.num2)
#         print("diff is",self.num1-self.num2)
#         print("quot is",self.num1/self.num2)
#
#
#
# a=Calculator()
# a.calci(10,20)
# a.calculate()



#
# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#
#     def add(self):
#         return self.num1+self.num2
#
#     def diff(self):
#         return self.num1-self.num2
#
#     def pro(self):
#         return self.num1*self.num2
#
#     def quot(self):
#         return self.num1/self.num2
#
#
# b=Calculator(3,7)
# print(b.add())
# print(b.pro())


# class Book:
#     def __init__(self,a_name,b_name,chapters,pages,books_sold):
#         self.a_name=a_name
#         self.b_name=b_name
#         self.chapters=chapters
#         self.pages=pages
#         self.books_sold=books_sold
#
#     def printbook(self):
#         print("Author name : ",self.a_name)
#         print("Book name : ",self.b_name)
#         print("Total Chapters : ",self.chapters)
#         print("Total pages : ",self.pages)
#         print("Total books sold : ",self.books_sold)
#
# a=Book("JK Rowling","Harry Potter and the Chamber of Secrets",18,251,"77 Million copies")
# a.printbook()

# class Employee:
#     def employee(self,name,id):
#         self.name=name
#         self.id=id
#     def __str__(self):
#         return self.name + str(self.id)
#
# a=Employee()
# a.employee("Jain ",21)
# print(a)

#
# class Parent:
#     def parent(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def printp(self):
#         print(self.name,self.age,self.gender)
#
# class Child(Parent):
#     def child(self,cname,cage,cgender):
#         self.cname=cname
#         self.cage=cage
#         self.cgender=cgender
#     def printc(self):
#         print(self.cname,self.cage,self.cgender)
#
# a=Child()
# a.parent("Mini",47,"Female")
# a.child("Janet,",24,"Female")
# a.printp()
# a.printc()

















