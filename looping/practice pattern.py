for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    for k in range(5,i,1):
        print(k,end=" ")
    print()