#recursion
n=10
sum=0
for i in range(n):
    sum=sum+i+1
print(sum)

#now recursion
def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)
    
print(sum(10))