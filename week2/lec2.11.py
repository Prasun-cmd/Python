# diferent types of import library
'''import calendar   # we can also write import calendar as c so we use c as calander as keywords
#this import the entire library so we have to use calender for every time we use

#print(calendar.month(2021,1))
print(calendar.calendar(2024)) '''

from calendar import* # here calander lib in import for below code so we doesn't require calander word 
print(calendar(2024))
print(month(2024,1))
#* is used to use all the feature if we write only month or calander we only use this only

print(month(2024,3))
import calendar as c
print(c.month(2024,4))

from random import*
print(random())
print(randrange(1,7))