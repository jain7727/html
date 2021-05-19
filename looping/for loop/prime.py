num=int(input("enter the num"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
if(flag==1):
    print("composite")
else:
    print("prime")


