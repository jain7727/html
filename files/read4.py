f=open("data1","r")
dic={}
lst=[]
data=[]
for i in f:
    data=i.rstrip("\n").split(",")
    # print(data)
    lst=data[4]
    print(lst)
    if data[4] not in dic:
        dic[data[4]]=1
    else:
       dic[data[4]]+=1
print(dic)



# words=line.split(" ")
# print(words)
#
# dic={}
# for i in words:
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]+=1
#
# print(dic)
#