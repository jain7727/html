
gender=(input("enter the gender"))
age=int(input("enter the age"))
print(gender,age)
if(gender=='F'):
    print("She will work only in urban areas")
elif(20<age<40):
    print("he may work anywhere")
elif(40<age<60):
    print("he will work only in urban areas")
else:
    print("error")

