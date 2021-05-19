# start=int(input("enter the starting limit:"))
# end=int(input("enter the ending limit:"))
# for i in range(start,end+1):
#     flag=0
#     for j in range(2,i):
#         if(i%j==0):
#             flag=1
#     if(flag==0):
#          print(i,end="  ")
#
#



# num=int(input("enter the limit:"))
#
# for i in range(2,num+1):
#     flag=0
#     for j in range(2,i):
#         if(i%j==0):
#             flag=1
#             break
#
#     if(flag==0):
#         print(i,end="  ")


# n=int(input("enter the year:"))
# if n%400==0:
#     print(n, "is a leap year")
# elif n%100==0:
#     print(n, "is not a leap year")
# elif n%4==0:
#     print(n, "is a leap year")
# else:
#     print(n, "is not a leap year")

# NumList = []
#
# Number = int(input("Please enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value of %d Element : " %i))
#     NumList.append(value)
#
# for i in range (Number):                  0 to 7
#     for j in range(i + 1, Number):         1 to 7
#         if(NumList[i] > NumList[j]):
#             temp = NumList[i]
#             NumList[i] = NumList[j]       2 5 7 1 9 3 6
#             NumList[j] = temp
#
# print("Element After Sorting List in Ascending Order is : ", NumList)

