# st=set()
# print(type(st))

st={1,2,4,"jain",2,True,3,4,"jain",False,10.5}
print(st)                                           # doesnt support duplicate value 1 means true 0 means false so <-


st1={9,8,7,6,5,4,3,2,1}
print(st1)

st1.add(10)              # adds an element using add function
print(st1)
                                             # set is mutable can be pushed or popped

st1.remove(8)             # pops out element using remove function
print(st1)

lst=[20,21,20,21,25,25,50,55,50]
st=set(lst)
print(st)

