#sort the given list
#low=0
#upp=len(lst)-1
#mid=low+upper//2
# 3 conditions  1. if element greater than mid assign low=mid+1
#               2. if element  lesser than mid assign upper=mid-1
#               3. if element equals mid element found


lst=[2,4,5,1,7,9,0]
lst.sort()
search=int(input("enter the element"))
low=0
upp=len(lst)-1

flag=0

while(low<=upp):
    mid=(low+upp)//2


    if (search > lst[mid]):
        low = mid + 1

    elif(search<lst[mid]):
        upp=mid-1

    elif(search==lst[mid]):
        flag=1
        break

if(flag>0):
    print("element found")
else:
    print("element not found")





#
# elif(search==lst[mid]):
#     print("element found")