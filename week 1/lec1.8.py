b=True #b is here a boolean type datatype
print(type(b))

#Type conversion
a=int(10.9) #here only int type that is 10 will consider and .9 will ignored
s=int('10')
print(a,type(a))
print(s,type(s))
f=float(9)
print(f,type(f))

a1=bool(10) #all value eexcept 0 is true
a2=bool(0)
a3=bool(-19)
a4=bool('0') #string representraion of 0 is always true
a5=bool('') #boolean coversion of empty string is false
print(a1,type(a1))
print(a2,(type(a2)))
print(a3,type(a3))
print(a4,type(a4))
print(a5,type(a5))
