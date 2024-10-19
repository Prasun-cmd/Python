#introduction to import library
import math
print(math.sqrt(4))
print(math.factorial(5))

import random 
print(random.random()) #gives random value btn 0 and 1


#Lets us simulate toss a coin

a=random.random()
print(a)
if(a<.5):
    print('heads')
else:
    print('tails')    

# dice simulation
print(random.randrange(1,7))