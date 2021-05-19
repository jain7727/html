




# def shuffle_values(func):
#     def wrappers(no1,no2):
#         if no1<no2:
#             no1,no2=no2,no1
#         return func(no1,no2)
#     return wrappers
# @shuffle_values
# def sub(num1,num2):
#     return num1-num2
# print(sub(2,10))
#
# @shuffle_values
# def div(num1,num2):
#     return num1/num2
# print(div(3,15))

#
# age=int(input("enter the age"))
# if age>=18:
#     print("eligible for vaccination")
# else:
#     raise Exception("NOt eligible for vaccination")

# def admin_req(func):
#     def wrapper(user,pin):
#         if user!="admin":
#             raise Exception("you are not allowed")
#         else:
#             return func(user,pin)
#     return wrapper
#
#
# @admin_req
# def change_pin(user,pin):
#     mypin=pin
#     return mypin
# print(change_pin("admin",1000))
#
# @admin_req
# def del_acc(user,accno):
#     return str(accno) + " deleted"
# print(del_acc("admin",1000))


# num1=int(input("enyer 1st num"))
# num2=int(input("enter 2nd num"))
# try:
#     div=num1/num2
#     print(div)
# except Exception as e:
#     print(e.args)

def vaccination(func):
    def vaccination1(**kwargs):
        age=kwargs["age"]
        health=kwargs["health"]
        if ((age>=65) | (health==True)):
            return func(**kwargs)
        else:
            raise Exception("u rnt lgble")
    return vaccination1()
@vaccination
def vaccination3(**kwargs):
    print("u r lgble")




vaccination3(name="Jain",age=69,place="Ernakulam",health=True)
