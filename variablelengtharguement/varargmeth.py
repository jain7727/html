# # def add_four(num1,num2,num3,num4):
# #     return num1+num2+num3+num4
# #
# # res=add_four(10,20,30,40)
# # print(res)
#
#
#
# # def add(*args):
# #     res=0
# #     for num in args:
# #         res+=num
# #     return res
# # print(add(1,3,5,9,1,90,54)
#
#
# # def mul(*args):
# #     res=1
# #     for num in args:
# #         res*=num
# #     return res
# # print(mul(1,2,3,4,5,6,7,8,9,10))
#
# # def print_employee(**kwargs):
# #     for k,v in kwargs.items():
# #         print(k,"->",v)
# # print_employee(id=10,native="kerala",studied="solapur")
# #
# # arr=[2,5,1,3,7,3]
# # print(arr.sort())
# # print(sorted(arr))
#
#
#
# # def print_employee(**kwargs):
# #     print(kwargs)
# #
# # print_employee(id=10,name="jain",loc="kl")
#
#
# employees = {
#     1000: {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
#     1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
#     1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
#     1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
#     1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
#
# }
#
# def print_employee(**kwargs):
#     id=kwargs["id"]
#     prop=kwargs["prop"]
#     if id in employees:
#               print(employees[id]["name"])
#               print(employees[id][prop])
#
#     else:
#         print("invalid id")
#
#
#
# print_employee(id=1002,prop="salary")
#

# def add(*arg):
#     result=0
#     for num in arg:
#         result+=num
#     return result
#
# print(add(1,2,3,4,5,6,7,8,9))


# def print_employee(**args):
#     print(args)
#
# print_employee(id=20,name="Jain",loc="Kochi")
#
#
#
#
# employees = {
#     1000: {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
#     1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
#     1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
#     1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
#     1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
#
# }
#
# eid=int(input("enter the id"))
# prop=input("enter the optional property")
# if (eid in employees)& (prop in employees[eid]):
#     print(employees[eid][prop])
# else:
#     print("Invalid eid")
# employees = {
#     1000: {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
#     1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
#     1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
#     1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
#     1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
#
# }
#
# def print_employee(**kwargs):
#     print(kwargs)
#     id=kwargs["eid"]
#     if(id in employees):
#         print(employees[id]["name"])
#     else:
#         print("invalid id")
# print_employee(eid=1002,prop="designation")
