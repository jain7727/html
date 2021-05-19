# import re
# text="hello23 world"
# x="[\D]"
# match=re.finditer(x,text)
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())


#
# import re
# numbers='''
# 123-456-7890
# 914.813.9330
# '''
# x="[\d\d\d.\d\d\d.\d\d\d\d]"
# match=re.finditer(x,numbers)
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())


# import re
# numbers='''
# 123-456-7890
# 914.813.9330
# '''
# pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# match=pattern.finditer(numbers)
# for i in match:
#     print(i)


import re
num=input("enter the number")
x="[\d\d\d[-.]\d\d\d[-.]\d\d\d\d]"
match=re.fullmatch(x,num)
for i in match:
    print("valid")
else:
    print("not valid")


