lines="ABCDBCA"
# words=lines.split(" ")
dic={}
flag=0
# for i in words:
#     if i not in dic:
#         dic[i]=1
#         flag=1
#
#
# if (flag==0):
#         print("first recursivce character is", i)


for char in lines:
    print(char)
    if char not in dic:
        dic[char]=1
    else:
        print(char,"is the recursive character")
        break




