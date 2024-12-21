#more on list
l1=[1,2,3]
l2=[20,30,40]
l12=l1+l2 #we can add list in this manner
l21=l2+l1
print(l12,l21)

l3=[1,2,3]*5
print(l3)

l4=[1,2,4]
l5=[4,2,1]
print(l4==l5)
print(l4>l5)

#list update

l6=[1,3,5]
l6[2]=7 #update the value in third position 
print(l6)

l7=[1,2,3]
l8=l7 #here internally same memory is used just name change 
#but in integer new memory is allocated
l7[0]=5
print(l7,l8)

#ways to allocate diffent memorty location'
l9=[1,2,3]
l10=list(l9)
l11=l9[:]
l12=l9.copy()

l10[0]=5
l11[1]=8
l12[2]=99
l13=l9
print(l9,l10,l11,l12)
print(l9 is l10) #ways to find wheter same memory location or not
print(l9 is l13)

#list is call by reference and integer is call by value

l14=[1,2,3]
l14.remove(2) # remove the element 2
l14.pop(0) #remove at the index 0
l14.insert(1,19) #insert at 2nd postion and 19
print(l14)