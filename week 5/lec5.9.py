#iterrator
fruits  =['mango','apple','guava','orange','watermelon','kiwi']
basket=iter(fruits)
print(next(basket))
print(next(basket))

#generator
def square(Limit):
    x=0
    while x<Limit:
        yield x*x
        yield x*x*x
        x+=1

a=square(5)
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))