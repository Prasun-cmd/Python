#tuples
t=(12,34,56,38,54,91)
print(t)
#tuples is unchangeable we cant append or remove
#we use tuples when we are sure that we dont not remove any things

import string
st=list(string.ascii_letters)
tp=tuple(st)

x="ram is a boy % * singer$$ ()"
p=list(x)
r=[]
for s in p:
    if s in tp:
     r.append(s)
print(r)

print(st.__sizeof__())
print(tp.__sizeof__()) #tuples take less space than list