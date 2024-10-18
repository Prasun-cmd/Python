#String Methods

x='pytHoN sTriNg MethOdS'

print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.title())
print(x.swapcase())

y='FAIR'
print(y.isupper())
print(y.islower())
print(y.istitle())

z='123'
t='abc'
f='abc34'
print(z.isdigit())
print(t.isalpha())
print(f.isalnum())

p='-----Python-----'
print(p.strip('-'))
print(p.lstrip('-'))
print(p.rstrip('-'))

print(p.startswith('-'))
print(p.endswith('n')) #also case sensitive

print(x.count('t'))
print(x.index('s'))
x=x.replace('S','s')
print(x)