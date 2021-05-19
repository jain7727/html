lst=[]
for i in range(1,101):
    lst.append(i)

flag=0
for i in lst:
    for j in (2,lst+1):
        if(i%j==0):
            flag=1
    if(flag==0):
        print(j)


# to be done later

