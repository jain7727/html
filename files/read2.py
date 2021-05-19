f=open("news","r")
lst=[]
for lines in f:
    lst.append(lines)
print(lst)

lst2=[]
for i in lst:
    words=i.split(" ")
    for j in words:
        lst2.append(j)
print(lst2)

dic={}
for i in lst2:
    if (i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
#
# words=lines.split(" ")
# print(words)
#
# dic={}
# for i in words:
#     if i not in lst1:
#         dic[i]=1
#     else:
#         dic[i]+=1
#
# print(dic)

