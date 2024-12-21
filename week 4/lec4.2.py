l=list(range(10))
print(l)
l.append('prasun')
l.append('India')
print(l)

print('prasun' in l)

#set
s={1,4,53,3,7,4,1}
print(type(s))
print(s) #set donot have repeat element
print(4 in s)

#searching in list is harder and in set is easy
#creating large list is easy but in set harder

import sys
x=list(range(1000))
s=set(range(1000))
print(sys.getsizeof(x)) #take smaller size
print(sys.getsizeof(s))#take larger size

#set is not subscriptable as s{0} gives error

z={'nitin',"neelam"}
z.add('prasun') #use to add element to set
print(z) 