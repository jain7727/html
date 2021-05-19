line="oyee lucky lucky oyee oyee lucky lucky oyee hello heya hello"
words=line.split(" ")
print(words)

dic={}
for i in words:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

print(dic)

#
# for i in dic:
#

