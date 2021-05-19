# cube=lambda num:num**4
# print(cube(6))


#
# lst1=[7,8,9,4,3,1]
# lst2=[]
# for num in lst1:
#     if num>5:
#         num+=1
#         lst2.append(num)
#     else:
#         num-=1
#         lst2.append(num)
#
# print(lst2)

# lst1=[7,8,9,4,3,1]
# op=[]
# for num in lst1:
#     op.append(num+1) if num>5 else op.append(num-1)
# print(op)

# lst1=[7,8,9,4,3,1]
# op=list(map(lambda num:num+1 if num>5 else num-1,lst1))
# print(op)

# check two lists are same or not
#
# lst1=[10,20,21,22,23]
# lst2=[20,21,10,22,23]
# a=sorted(lst1)
# print(a)
# b=sorted(lst2)
# print(b)
# if a==b:
#     print("Lists are same")
# else:
#     print("Lists arent same")




#Lambda function


# def cube(num):
#     return num**3
#
# print(cube(num=3))


# cube=lambda num:num**3
# print(cube(4))



# def div(num1,num2):
#     return num1/num2
# print(div(10,20))


#
# div=lambda num,num2:num/num2
# print(div(21,42))

# def first(str):
#     print(str[0])
# first("name")

# first=lambda str:str[0]
# print(first("Jain"))

#Map Function
# lst=[2,4,3,1,5]
# squares=list(map(lambda num:num**2,lst))
# print(squares)

# names=["arun","aravind","ajay"]
# upper=list(map(lambda name:name.upper(),names))
# print(upper)


#ternary operator

# num1=10
# num2=20
# large=num if num1>num2 else num2
# print(large)


# employees=[
#     {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
#     {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
#     {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
#     {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
#      {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
#
# ]
# emp_name=list(map(lambda emp:emp["name"],employees))
# print(emp_name)
#
# emp_sal=list(map(lambda emp:emp["salary"],employees))
# print(emp_sal)


#filter functions

# lst=[7,8,9,4,3,2]
# def chk_even(number):
#     return number%2==0
# evens=chk_even(filter())

# evens=list(filter(lambda number:number%2==0,lst))
# print(evens)
#
#
# grter=list(filter(lambda number:number>5,lst))
# print(grter)

# employees=[
#     {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
#     {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
#     {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
#     {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
#      {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
#
# ]
#
# # developers=list(filter(lambda emp:emp["designation"]=="developer",employees))
# # print(developers)
#
# name=list(filter(lambda emp:emp["designation"]=="developer",employees))
# developers_name=list(map(lambda emp:emp["name"],name))
# print(developers_name)


# import functools
# lst=[7,8,9,4,3,2]
# total=(functools.reduce(lambda no1,no2:no1+no2,lst))
# print(total)

# import functools
# lst=[7,8,9,4,3,2]
# highest=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
# print(highest)



#list comprehension   first the operation then the for loop or condition called

# lst=[1,2,3,4,5]
# sq=[num*num for num in lst]
# print(sq)

# fruits=["apple","orange","mango"]
# op=[(str,str) for str in fruits]
# print(op)

# lst=[10,20]
# lst2=[30,40]
# op=[(i,j) for i in lst for j in lst2 ]
# print(op)

# lst1=[1,2,3,4,5,6,7]
# even=[i for i in lst1 if i%2==0]   #here first for loop then condition
# print(even)

# lst=[7,8,9,4,3,2]
# op=[num+1 if num>5 else num-1 for num in lst]
# print(op)


employees=[
    {"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
     {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]
# emp_names=[emp["name"] for emp in employees]
# print(emp_names)

emp_details=[emp for emp in employees if emp["designation"]=="developer"]
print(emp_details)
high_sal=max([emp["salary"] for emp in employees])
print(high_sal)