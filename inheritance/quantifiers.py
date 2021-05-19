# import re
# x="a+"     #a including in group
# r="acg gdt gad wea"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())


#
# import re
# x="a*"     #a count including zero number of a
# r="acg gdt gad wea"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())

# import re
# x="a?"     #a count a as each including zero number of a
# r="acg  aaa gdt gad wea"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())

# import re
# x="a{2}"     #grouping of a in {?} when
#               # included will not include nxt time
#
# r="acaa baab gaga aa"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())


# import re
# x="a{1,3}"     #a minimum 2 maximum 3
# r="acaa baaaab gaga aaaa"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())


# import re
# x="^a"     # check starting with a
# r="acaa baaab gaga aa"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())

# import re
# x="a$"     # check ending with a
# r="acaa baaab gaa"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())



# import re
# x="^a"     # check starting with a
# r="acaa baaab gaga aa"
# match=re.finditer(x,r)
# for i in match:
#     print(i.start(),end=" ")
#     print(i.group())

#
# import re
# n="57kg 5fg"
# x="\w*"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


#
# import re
# n="57kg"
# x="\d{2}[a-z]{2}"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# import re
# n=input("enter the cell number")
# x="\d{10}"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# import re
# n=input("enter the cell number")
# x="^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


#check cell no starting with+91
# import re
#
# n = input("enter the cell number")
# x ="[+][9][1][\s]\d{10}"
# match = re.fullmatch(x, n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

#combination ending with number
# import re
# n=input("enter the combination")
# x="[a-zA-Z]+[0-9]$"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

#combination starting with a and ending with b
# import re
# n=input("enter the combination")
# x="^a*[a-zA-Z0-9\W]*b$"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")

#
# import re
# n=input("enter the combination")
# x="([a-zA-Z]{8,15})"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")



# # vehicle registration of kerala
# import re
# n=input("enter the combination")
# x="[K][L]+([0-9]{2})+([A-Z]{2})+([0-9]{1,4})"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")



# import re
# n=input("enter the combination")
# x="([a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+)"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("not valid")






