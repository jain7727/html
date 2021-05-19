f=open("numbers","r")
lst=[]
for lines in f:
    lst.append(int(lines.rstrip("\n")))

print(lst)
print(sum(lst))

data="hello"
data1=data.strip("ho")
print(data1)


# to remove an end character or \n use function rstrip()