# Find whether the given number is odd or even
'''
num=int(input('Enter the Number:'))
if(num%2==0):
    print('Even')
else:
    print('odd')    '''


 # find whether the given number ends with 0 or 5 or any other
'''                                            
num=int(input('Enter the number: '))

if(num%5==0):
    if(num%10==0):
        print('0')
    else:
        print('5')    

else:
    print('other')        '''

#Find the grade of the student based on the given marks from 0 to 100

marks=int(input('Enter Your marks:'))
if(100>=marks>=0):
    if(marks>=90):
        print("A")
    elif(marks>=80):
        print("B")
    elif(marks>=70):
        print("C")
    elif(marks>=60):
        print("D")  
    else:
        print('E')  
else:
    print("Invalid input")
