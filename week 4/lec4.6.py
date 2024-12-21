#more on tuples
t=1,2,4 #tuples is used in packing
print(t,type(t))
x,y,z=t # tuples is used in unpacking
print(x,y,z)

l=[10]
print(l,type(l))

t=(12) #single element in tuples acts as int
print(t,type(t))

tp=([1,2],['a','b'])
tp[0][0]=10 #we can change list inside tuples thius is call non hashable
print(tp)

t1=(1,2,3) #this is hashable 
t2=([1,2,3],)#this is non hashable