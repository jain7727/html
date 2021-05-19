num1=int(input("enter the first no"))
num2=int(input("enter the second no"))
num3=int(input("enter the third no"))

print(num1,num2,num3)

if(num1>num2>num3):
    print("2nd largest no is ", num2)
elif(num2>num3>num1):
    print("2nd largest no is ", num3)
else:
    print(num1)