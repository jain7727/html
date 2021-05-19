num1=int(input("enter the mark of 1st subj"))
num2=int(input("enter the mark of 2nd subj"))
num3=int(input("enter the mark of 3rd subj"))
num4=int(input("enter the mark of 4th subj"))

total=num1+num2+num3+num4
print(total)

if((total>=180) & (total<=200)):
     print("A+")
elif((total>=160) & (total<=179)):
     print("A")
elif ((total >= 140) & (total <= 159)):
     print("B+")
elif ((total >= 120) & (total <= 139)):
     print("B")
elif ((total >= 100) & (total <= 119)):
     print("C+")
elif ((total >= 80) & (total <= 99)):
     print("C")
elif ((total >= 68) & (total <= 79)):
     print("D+")
else:
    print("Fail")

