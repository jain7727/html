#overloading

# class Student:
#     def students(self,name,rollno,dept,marks):
#         self.name=name
#         self.rollno=rollno
#         self.dept=dept
#         self.marks=marks
#         print("Name : ",self.name)
#         print("Roll no : ",self.rollno)
#         print("Department : ",self.dept)
#         print("Marks : ",self.marks)
#
# class Child(Student):
#     def students(self,cname,cage):
#         self.cname=cname
#         self.cage=cage
#         print(self.cname,self.cage)
#
# ch=Child()
# ch.students("jain",23,"badu",24)


# over riding

class Parent:
    def properties(self):
        print("hello")

    def set(self):
        print("hello 1")

class Child(Parent):
    def set(self):
        print("hello 2")

b=Child()
b.set()
b.properties()





# f=open("students","r")
# for i in f:
#     d=(i.rstrip("\n").split(","))
#     name=d[0]
#     rollno=d[1]
#     dept=d[2]
#     marks=d[3]
#     obj=Student()
#     obj.students(name,rollno,dept,marks)
#     if int(d[3])>190:
#         obj.printstudents()
#
# class Student:
#     def student(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         print(self.name,self.rollno)
#
# class Student2(Student):
#     def student(self,id,loc):
#         self.id=id
#         self.loc=loc
#         print(self.id,self.loc)
#
#
#
# a=Student2()
# a.student(21,"Flat no 10")


# class Students:
#     def students(self,name,rollno,stream,marks):
#         self.name=name
#         self.rollno=rollno
#         self.stream=stream
#         self.marks=marks
#
# class Student:
#     def student(self,name,rollno,dept,marks):
#         self.name=name
#         self.rollno=rollno
#         self.dept=dept
#         self.marks=marks
#     def printstudents(self):
#         print(self.name, self.rollno)
#
#
# f=open("students","r")
# for i in f:
#     d = (i.rstrip("\n").split(","))
#     print(d)
#     # name = d[0]
#     # rollno = d[1]
#     # dept = d[2]
#     # marks = d[3]
#     # obj = Student()
#     # obj.student(name, rollno, dept, marks)
#     # if int(d[3]) > 190:
#     #     obj.printstudents()











