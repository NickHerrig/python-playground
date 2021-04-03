As Peter Norvig pointed out a couple of years after the classic Design 
Patterns book appeared, “16 of 23 patterns have qualitatively simpler 
implementation in Lisp or Dylan than in C++ for at least some uses of 
each pattern (slide 9 of Norvig’s “Design Patterns in Dynamic Languages
presentation). Python shares some of the dynamic features of the Lisp and
Dylan languages, in particular first-class functions, our focus in this 
part of the book.

From the same talk quoted at the start of this chapter, in reflecting on 
the 20th anni‐ versary of Design Patterns: Elements of Reusable 
Object-Oriented Software, Ralph Johnson has stated that one of the 
failings of the book is “Too much emphasis on pat‐ terns as end-points 
instead of steps in the design process.”5 In this chapter, we used the 
Strategy pattern as a starting point: a working solution that we could 
simplify using first-class functions.

In many cases, functions or callable objects provide a more natural way 
of imple‐ menting callbacks in Python than mimicking the Strategy or the 
Command patterns as described by Gamma, Helm, Johnson, and Vlissides. 
The refactoring of Strategy and the discussion of Command in this 
chapter are examples of a more general insight: sometimes you may 
encounter a design pattern or an API that requires that components 
implement an interface with a single method, and that method has a 
generic-sounding name such as “execute”, “run”, or “doIt”. Such patterns 
or APIs often can be implemented with less boilerplate code in Python 
using first-class func‐ tions or other callables.

The message from Peter Norvig’s design patterns slides is that the 
Command and Strategy patterns—along with Template Method and Visitor can 
be made simpler or even “invisible” with first-class functions, at least 
for some applications of these patterns.
