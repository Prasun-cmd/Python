def myfunction1(x):
    x=x*2 #here x is local variable
    print('value of x in function 1',x)
def myfunction2(x):
    x=x*3
    print('value of x in function 2',x)

x=5 #here x is global variable
print('value of x before function call',x)
myfunction1(x)
myfunction2(x)
print('value of x after function call',x)

def myfunction1():
    global x
    x=x*2 #here x is global variable
    print('value of x in function 1',x)
def myfunction2():
    global x
    x=x*3
    print('value of x in function 2',x)

x=5 #here x is global variable
print('value of x before function call',x)
myfunction1()
myfunction2()
print('value of x after function call',x)

