st={1,2,3,4,5,6,7,8,9}
print(st)

st.update([10,11,12])
print(st)                         # pushing multiple elements(update function

st.discard(10)
print(st)

st.pop()
print(st)

st={1,2,3,4,5,12,10,6,7,8,9}
st1={10,11,12,13,14}

st2=st.union(st1)
print(st2)

st3=st.intersection(st1)
print(st3)

st4=st.difference(st1)
print(st4)



