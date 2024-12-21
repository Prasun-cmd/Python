f=open('mytext.txt','r')
flag=0
s='0'
while(s!=''):
    s=f.readline()
    if(s=='haii'):
        print('found')
        flag=1
        break
if(flag==0):
    print('not found')
