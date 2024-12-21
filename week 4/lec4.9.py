def list_maxi(l):
    maxi=l[0]
    for i in range(len(l)):
        if(l[i]>maxi):
            maxi=l[i]
    return maxi

l=[2,67,43,89,21]
print(list_maxi(l))

def average(l):
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    return sum/len(l)

print(average(l))