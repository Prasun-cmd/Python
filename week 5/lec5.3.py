def ovious_sort(l):
    x=[]
    while(len(l)>0):
        min=l[0]
        for i in range(len(l)):
            if (l[i]<min):
                min=l[i]
        x.append(min)
        l.remove(min)
    return x

l=[23,65,34,76,55,33]
print(ovious_sort(l))