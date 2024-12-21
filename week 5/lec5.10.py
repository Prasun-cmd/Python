#lambda function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

print(add(10,20))
print(sub(12,6))

#now 
add=lambda a,b:a+b
sub=lambda a,b:a-b

print(add(12,13))
print(sub(12,8))

#enumerate function

fruits  =['mango','apple','guava','orange','watermelon','kiwi']

for i in fruits:
    print(i)
#we want to know the index

for i in enumerate(fruits): #create a tupples along with index

    print(i)

#zip
size=[3,7,8,5,7,4]
print(list(zip(fruits,size)))
print(dict(zip(fruits,size)))   

#map
a=[2,6,7,5,2,5,7,8]
b=[1,6,5,8,4,2,2,1]
#c=a-b this cant be done

def sub(x,y):
    return x-y
c=map(sub,a,b)
print(list(c))

#filter function
import math
a=[25,-16,144,-100]

def square_root(n):
    return math.sqrt(n)

def ispositive(n):
    if n>=0:
        return n

c=map(square_root,filter(ispositive,a))
print(list(c))