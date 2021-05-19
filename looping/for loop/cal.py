ll=int(input("enter the limit"))
ul=int(input("enter the limit"))
sumofeven=0
sumofodd=0
for i in range(ll,ul+1):
    if(i%2==0):
        sumofeven=sumofeven+i
    else:
        sumofodd=sumofodd+i
print(sumofeven)
print(sumofodd)



