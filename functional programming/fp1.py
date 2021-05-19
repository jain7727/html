# # f=lambda x,y:x+y
# # print(f(20,29))
# # f=lambda x,y:x-y
# # print(f(20,29))
# # f=lambda x,y:x*y
# # print(f(20,29))
# # f=lambda x,y:x/y
# # print(f(20,29))
#
#
# #map(fn,iterable)
# #filter(fn,iterable)
# # lst=[21,22,23,24,25,26,27,28,29]
#
# # def sq(num):
# #     return num*num
# #
# #
# # s=list(map(sq,lst))
# # print(s)
# #
# # s=list(map(lambda num:num*num,lst))
# # print(s)
# # # filter
# # def sq(num):
# #     return num%2==0
# #
# #
# # s=list(filter(sq,lst))
# # print(s)
# #
# #
# #
# # lst=[21,22,23,24,25,26,27,28,29]
# #
# # s=list(filter(lambda num:num%2==0,lst))
# # print(s)
#
# #list comprehension
#
# newlist=[]
# for i in range(1,51):
#     newlist.append(i)
# print(newlist)
#
#
# lst=[i for i in range(1,21)]
#
# print(lst)
#
#
# lst1=[i*i if i%2==0 else i*i*i for i in range(1,21)]
# print(lst1)
#
#
# lst2=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,21)]
# print(lst2)
#
#
#

# a=10
# def printa():
#     a=2
#     global a
#     # print(a)
# printa()
# print(a)


stack=[]
size=int(input("enter the size"))
top=0
n=0



def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        a = int(input("enter the element to be inserted"))
        stack.append(a)
        top += 1
        print(stack)







def pop():
    global top, size
    if top <= 0:
        print("stack is empty")
    else:

        stack.pop()
        top-=1
        print(stack)




while n!=1:
    print("enter the operation to be done")
    operation=int(input("1)PUSH  2)POP"))
    if operation==1:
        push()
    else:
        pop()


#
# queue=[]
# top=0
# n=0
# size=int(input("enter the size"))
#
#
#
# def insert():
#     global top,size
#     if top>=size:
#         print("queue is full")
#     else:
#         b=int(input("enter the element to be inserted"))
#         queue.insert(b)
#         top+=1
#         print(queue)
#
# def delete():
#     global top,size
#     if top<=0:
#         print("queue is empty")
#     else:
#         queue.clear()
#         top-=1
#         print(queue)
#
#
#
# while n!=1:
#     print("enter the operation")
#     a=int(input("1) insert  2)delete"))
#     if a==1:
#         insert()
#     else:
#         delete()



















