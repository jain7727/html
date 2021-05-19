employee={"id":10,"name":"Jain","designation":"student","salary":0}
print(employee)

print(employee["name"])
print("company" in employee)

employee["company"]="apple"
print(employee)

employee["salary"]+=5000
print(employee)

for i in employee:
    print(i, ":", employee[i])

