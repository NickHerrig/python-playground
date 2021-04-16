# Chapter Summary

We covered a lot of ground in this chapter, but I tried to make the 
journey as smooth as possible even if the terrain is rugged. After all, 
we did enter the realm of metaprogramming.

We started with a simple @register decorator without an inner function, 
and finished with a parameterized @clock() involving two levels of nested
functions.

Registration decorators, though simple in essence, have real applications
in advanced Python frameworks. We applied the registration idea to an 
improvement of our Strategy design pattern refactoring from Chapter 6.

Parameterized decorators almost aways involve at least two nested 
functions, maybe more if you want to use @functools.wraps to produce a 
decorator that provides better support for more advanced techniques. One 
such technique is stacked decorators, which we briefly covered.

We also visited two awesome function decorators provided in the functools
module of standard library: `@lru_cache()` and `@singledispatch`.

Understanding how decorators actually work required covering the 
difference between import time and runtime, then diving into variable 
scoping, closures, and the new nonlocal declaration. Mastering closures 
and nonlocal is valuable not only to build decorators, but also to code 
event-oriented programs for GUIs or asynchronous I/O with callbacks.
