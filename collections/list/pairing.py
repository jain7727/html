lst=[1,2,3,4,5,6]
element=int(input("enter the element"))
flag=0

for i in lst:
    for j in lst:
        if(i+j==element):
            print(i)
            print(j)
    break



