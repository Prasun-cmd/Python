#Exception handling
#zero exception handling
a=int(input())
b=int(input())
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print('invalid input')
except NameError:
    print('variable not thre')
finally:
    print('all ok')


#user define exception
a=int(input())
if(a<18):
    raise Exception('you are under age')