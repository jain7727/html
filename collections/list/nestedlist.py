lst=[[1,'jain',23,1000],[2,'owais',22,2000],[3,'bilal',22,3000],[4,'rishi',23,4000]]
for i in lst:
    print(i)

for emp in lst:
    if (emp[3]>2000):
        print(emp[1])

sum=0
for emp in lst:
    sum+=emp[3]
print(sum)
    