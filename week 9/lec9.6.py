#sorting recursively

def mini(l):
   mini=l[0]
   for x in l:
    if(x<mini):
        mini=x
   return mini

def sort(l):
    if len(l)<=1:
        return l
    m=mini(l)
    l.remove(m)     
    return [m]+sort(l)

l=[8,96,56,4,6]
print(sort(l))


