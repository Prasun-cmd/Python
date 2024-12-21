# find prime number less than given number
"""num=int(input("enter the number "))
if(num>2):
    print(2, end=' ')
for i in range(3,num):
    flag=False
    for j in range(2,i):
        if(i%j==0):
         flag=False
         break
        else:
           flag=True
    if(flag==True):
       print(i, end=' ')
print(' ')       
#finding total trade amount for trader

empID=input('Enter the employee ID ')
while(empID!=-1):
   trade=int(input('Enter the trade amount '))
   prf_l=0
   while(trade!=0):
      prf_l=prf_l+trade
      trade=int(input('enter the trade amount '))
   print(f'profit/loss of empyee of ID {empID} is {prf_l}')
   empID=input('Enter the employee Id')"""
         
    
"""#total rainfall calculation
dur=int(input('enter the duration for rainfall '))
for i in range(1,dur+1):
    rain=int(input('enter the rain '))
    train=0
    while(rain!=-1):
        train=train+rain
        rain=int(input('ENTER THE RAIN'))
    print(f'the total rain in day{i} is {train}')"""

#finding largest string in all until -1
word=str(input('enter the word '))
while(word!='-1'):
    long=0
    if(len(word)>long):
        long=len(word)
    word=input('enter the word ')
print('thw longest word is {0}'.format(long))