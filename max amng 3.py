num1=int(input("enter fst num"))
num2=int(input("enter snd num"))
num3=int(input("enter thd num"))

if((num1>num2) & (num1>num3)):
    print("num1 is greater than all")
elif((num2>num1) & (num2>num3)):
     print("num2 is greater than all")
else:
      print("num3 is greater than all")