a=10
b=20
"""if a<b:
    small=a
else:
    small=b"""
small=a if a<b else b
print(small)

a=5
while(a>0):
    print(a)
    a-=1
a=5
while a>0:print(a);a-=1

#list comprehension
fruits  =['mango','apple','guava','orange','watermelon','kiwi']
'''newlist=[]
for fruit in fruits:
    if 'n' in fruit:
        newlist.append(fruit.capitalize())
print(newlist)'''
newlist=[fruit.capitalize() for fruit in fruits if 'n' in fruit]
print(newlist)
