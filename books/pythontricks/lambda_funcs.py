
# example simple lambda function
add = lambda x, y: x + y

# The same lambda funciton, but showing that you can call directly will out assinging it to a name. 
print((lambda x, y: x + y)(3,4))


# you could use lambdas... but maybe you shouldn't?
print(list(filter(lambda x: x % 2 == 0, range(16))))

# in many cases list comps or generator expressions are cleaner and less magical. 
print([x for x in range(16) if x % 2 ==0])
