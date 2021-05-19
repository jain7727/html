# a=int(input("enter a no"))
# b=int(input("enter a no"))
#
#
# try:                                      # give codes which may occur error in try block . Try block always works
#                                           # if any happens jumps to except block
#     print(a/b)
#
# except:
#     print("exception occured")
#


lst=[2,3,4]
a=int(input("enter the index"))#EXCEPTIONAL HANDLING

try:
    # print(lst[2])
    print(lst[a])
except:
    print("list index out of range")

finally:
    print("worked")