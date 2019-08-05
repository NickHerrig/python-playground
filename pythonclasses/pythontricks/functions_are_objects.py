
def yell(text):
    return text.upper() + '!'

def wisper(text):
    return text.lower() + '...'

# you can assign functions to other variables
x = yell
y = wisper

print(x("hello world"))
print(y('HELLO WORLD'))

# you can also access the string ientifier of the function
print(x.__name__)
print(y.__name__)


# functions can be stored in data structures aswell
funcs = [yell, wisper]
funcstup = (yell, wisper)

print(funcs, type(funcs))
print(funcstup, type(funcstup))

print("list loop:")
for func in funcs:
    print(func, func('hello world'))

print("tuple loop:")
for func in funcstup:
    print(func, func('HELLO WORLD'))

# functions can be passsed to other functions
# These functions are also knowns as higher order functions
def greet(function):
    greeting = function('Hello, world.')
    print(greeting)

greet(yell)
greet(wisper)


# functions can be nested
def get_speak_func(volume):
    def wisp(text):
        return text.lower() + '...'
    def loud(text):
        return text.upper() + '!'
    if volume > .5:
        return loud
    else:
        return wisp

print(get_speak_func(.2))


# Functions that remember values from lexical scope are called closures. 
def get_speak_func(text, volume):
    def wisp():
        return text.lower() + '...'
    def loud():
        return text.upper() + '!'
    if volume > .5:
        return loud
    else:
        return wisp

print(get_speak_func('Hello world', .2)())
print(get_speak_func('Hello world', .7)())


# Objects can behave like functions and can be callable with dunder call method.

class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)
print(plus_3(4))

print(Adder(3)(4))
