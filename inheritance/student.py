
class Student:
    def student(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def printstudent(self):
        print("Name : ",self.name)
        print("Roll no :",self.rollno)


f=open("student","r")
for i in f:
    d=(i.rstrip("\n").split(","))
    # print(d)
    name=d[0]
    rollno=d[1]
    obj=Student()
    obj.student(name,rollno)
    obj.printstudent()






