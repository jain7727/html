num1=int(input("enter the number of classes held"))
num2=int(input("enter the number of classes attended"))

num3=(num2/num1)*100
print(num3)
if(num3<75):
    print("following candidate is not allowed for the exam")
else:
    print("candidate is allowed for the foll")

