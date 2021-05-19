lst=[4,8,4]
newlst=[]
sum=0

for i in lst:
    sum+=i

for i in lst:
    newlst.append(sum-i)

print(newlst)