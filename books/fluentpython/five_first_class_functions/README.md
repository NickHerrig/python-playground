Chapter 5 - First Class Functions

The goal of this chapter was to explore the first-class nature of 
functions in Python. The main ideas are that you can assign functions 
to variables, pass them to other functions, store them in data structures,
and access function attributes, allowing frameworks and tools to act on 
that information. Higher-order functions, a staple of functional 
programming, are common in Python--even if the use of map, filter, and 
reduce is not as frequent as it was-—thanks to list comprehensions 
(and similar constructs like generator expressions) and the appearance of
reducing built-ins like sum, all, and any. The sorted, min, max built-ins,
and functools.partial are examples of commonly used higher-order functions
in the language.

Callables come in seven different flavors in Python, from the simple 
functions created with lambda to instances of classes implementing 
__call__. They can all be detected by the callable() built-in. Every 
callable supports the same rich syntax for declaring formal parameters,
including keyword-only parameters and annotations— both new features 
introduced with Python 3.

Python functions and their annotations have a rich set of attributes that
can be read with the help of the inspect module, which includes the 
Signature.bind method to apply the flexible rules that Python uses to bind
actual arguments to declared parameters.

Lastly, we covered some functions from the operator module and 
functools.partial, which facilitate functional programming by minimizing 
the need for the functionally challenged lambda syntax.
