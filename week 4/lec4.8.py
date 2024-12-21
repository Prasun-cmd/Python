def add(a,b):
    ans=a+b
    return ans

def sub(c,d):
    ans=c-d
    return ans


def discount(cost,d):
    price=cost-(cost*(d/100))
    return price

print(add(5,9))
print(sub(9,2))
print(discount(100,9))

print(add(7,9)+sub(9,3)+discount(100,8))