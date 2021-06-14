This chapter started easily enough with discussion of else 
blocks in for, while, and try statements. Once you get used to
the peculiar meaning of the else clause in these statements, I
believe else can clarify your intentions.

We then covered context managers and the meaning of the with 
statement, quickly moving beyond its common use to 
automatically close opened files. We implemented a custom 
context manager: the LookingGlass class with the 
__enter__/__exit__ methods, and saw how to handle exceptions 
in the __exit__ method. A key point that Raymond Hettinger made
in his PyCon US 2013 keynote is that with is not just for 
resource management, but it’s a tool for factoring out common 
setup and teardown code, or any pair of operations that need to
be done before and after another procedure 

Finally, we reviewed functions in the contextlib standard 
library module. One of them, the @contextmanager decorator, 
makes it possible to implement a context manager using a simple
generator with one yield—a leaner solution than coding a class
with at least two methods. We reimplemented the LookingGlass as
a looking_glass generator function, and discussed how to do 
exception handling when using @contextmanager.

The @contextmanager decorator is an elegant and practical tool
that brings together three distinctive Python features: a 
function decorator, a generator, and the with statement.
