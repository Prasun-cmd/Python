l=['It','was','Monday','morning','Swaminathan','was','reluctant','to','open','his','eyes','he','considered','Monday','specially','unpleasant','in','the','calander','After','the','delicious','freedom','of','Saturday','and','Sunday','it','was','difficult','to','get','into','the','Monday','mood','of','work','and','discipline','He','shuddered','at','the','very','thought','of','school','the','dismal','yellow','building','the','fire','eyed','Vedanayagam','his','class','teacher','and','headmaster','with','his','thin','long','cane']
print(l,(len(l)))
s=set(l)
print(s,len(s))
max=0
word=''
d={}
for x in s:
    d[x]=0

for x in l:
    d[x]=d[x]+1
    if d[x]>max:
        max=d[x]
        word=x
print(max,word)

