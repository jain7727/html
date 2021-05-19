f=open("data","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    fname=data[1]
    age=data[3]
    country=data[-1]

    lst=([fname,age,country])
    for i in lst:
        if (lst[2]=="india"):
              print(lst)



