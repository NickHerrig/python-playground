We started this chapter by reviewing some restrictions Python imposes on 
operator overloading: no overloading of operators in built-in types, and 
overloading limited to existing operators, except for a few ones (is, and,
or, not).

We got down to business with the unary operators, implementing __neg__ and
__pos__. Next came the infix operators, starting with +, supported by the
__add__ method. We saw that unary and infix operators are supposed to 
produce results by creating new objects, and should never change their 
operands. To support operations with other types, we return the 
NotImplemented special value—not an exception— allowing the interpreter to
try again by swapping the operands and calling the reverse special method
for that operator (e.g., __radd__). The algorithm Python uses to handle 
infix operators is summarized in the flowchart in Figure 13-1.

Mixing operand types means we need to detect when we get an operand we 
can’t handle. In this chapter, we did this in two ways: in the duck typing
way, we just went ahead and tried the operation, catching a TypeError 
exception if it happened; later, in __mul__, we did it with an explicit is
instance test. There are pros and cons to these approaches: duck typing is
more flexible, but explicit type checking is more predictable. When we did
use isinstance, we were careful to avoid testing with a concrete class, 
but used the numbers.Real ABC: isinstance(scalar, numbers.Real). This is a
good compromise between flexibility and safety, because existing or future
user-defined types can be declared as actual or virtual subclasses of an 
ABC, as we saw in Chapter 11.

The next topic we covered was the rich comparison operators. We 
implemented == with __eq__ and discovered that Python provides a handy 
implementation of != in the __ne__ inherited from the object base class. 
The way Python evaluates these operators along with >, <, >=, and <= is 
slightly different, with a different logic for choosing the reverse method
, and special fallback handling for == and !=, which never generate errors
because Python compares the object IDs as a last resort.

In the last section, we focused on augmented assignment operators. We saw
that Python handles them by default as a combination of plain operator 
followed by assignment, that is: a += b is evaluated exactly as a = a + b.
That always creates a new object, so it works for mutable or immutable 
types. For mutable objects, we can implement inplace special methods such
as __iadd__ for +=, and alter the value of the lefthand operand. To show 
this at work, we left behind the immutable Vector class and worked on 
implementing a BingoCage subclass to support += for adding items to the 
random pool, similar to the way the list built-in supports += as a 
short‐cut for the list.extend() method. While doing this, we discussed how
+ tends to be stricter than += regarding the types it accepts. For 
sequence types, + usually requires that both operands are of the same type
, while += often accepts any iterable as the righthand operand.
