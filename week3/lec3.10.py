# for loop is more useful when we know the number of iteration 

#factorial using for lopp
num=int(input("Enter the Number :"))
fact=1
if(num<0):
    print("Invalid input")

else:
   for i in range(num,1,-1):
       fact=fact*i

print(fact)

