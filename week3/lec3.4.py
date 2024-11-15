#Find number of digit in given number
'''   num=abs(int(input("enter the number: ")))
    digit=1

    while(num>9):
        num=num //10
        digit=digit+1
    print(digit)    '''

#Find the reverse of the given number
num=int(input("Enter the number: "))
absnum=abs(num)

rev=absnum%10
absnum=absnum//10
while(absnum>0):
        r=absnum%10
        absnum=absnum//10
        rev=rev*10+r 

if(num>=0):
    
    print(rev)                                                                

else:  
    
    print(rev-2*rev)      