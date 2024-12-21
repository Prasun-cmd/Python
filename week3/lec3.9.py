for x in range(10):
 print(x) 
for x in range(10):
 print(x, end=' ') #this will print the number in same line
print('')

d=12
m=6
y=2024

print('today date is',d,m,y)
print('today date is',d,m,y,sep='/')
print('today date is ',end='')
print(d,m,y, sep='/')
print('r')
num=int(input())
for i in range(1,11):
    #print(num,'X',i,'=',num*i)
    #print(f'{num} X {i} = {num*i}')
    #print('{0} X {1} = {2}' .format(num,i,num*i))
    print('%d X %d = %d'%(num,i,num*i))

pi=22/7
print(f'the value of pi = {pi}')
print('the value of pi is {0}'.format(pi))
print('the value of pi =%f' %(pi))

print(f'the value of pi = {pi:.2f}')
print('the value of pi is {0:.2f}'.format(pi))
print('the value of pi =%.2f' %(pi))


print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))
print('{0}'.format(1111))
print('{0}'.format(11111))

print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))

print('{0:5s}'.format('*'))
print('{0:5s}'.format('**'))
