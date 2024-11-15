#sum of first n integer using for loop

n=int(input("Enter the number:"))
sum=0
for i in range(n+1):
    sum=sum+i

print('Sum of n integer is:',sum)    