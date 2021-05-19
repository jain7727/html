# dictionary
 #dic={}     syntax
  # key-value pairs
  # insertion order preserved
  #doesnt support duplicate key

dic = {"name": "Jain", "id": 10, "loc": "Mh", "marks": 0,"data": 10.70, "result": False}
for i in dic:
    print(i, end=" : ")
    print(dic[i])





print(dic["name"],dic["loc"],dic["data"])

print(dic["loc"])

dic["id"]=12
dic["marks"]=10
print(dic)

dic.pop("marks")      # deletes an element
del dic["name"]
print(dic)

print("total" in dic)

dic["total"]=150
print(dic)

