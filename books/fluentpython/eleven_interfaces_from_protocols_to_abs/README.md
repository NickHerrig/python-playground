The goal of this chapter was to travel from the highly dynamic nature of 
informal interfaces (called protocols) visit the static interface 
declarations of ABCs, and conclude with the dynamic side of ABCs: virtual
subclasses and dynamic subclass detection with __subclasshook__.

We started the journey by reviewing the traditional understanding of 
interfaces in the Python community. For most of the history of Python, 
we’ve been mindful of interfaces, but they were informal like the 
protocols from Smalltalk, and the official docs used language such as 
“foo protocol,” “foo interface,” and “foo-like object” interchangeably. 
Protocolstyle interfaces have nothing to do with inheritance; each class 
stands alone when implementing a protocol. That’s what interfaces look 
like when you embrace duck typing.

With Example 11-3, we observed how deeply Python supports the sequence 
protocol. If a class implements __getitem__ and nothing else, Python 
manages to iterate over it, and the in operator just works. We then went 
back to the old FrenchDeck example of Chapter 1 to support shuffling by 
dynamically adding a method. This illustrated monkey patching and 
emphasized the dynamic nature of protocols. Again we saw how a partially 
implemented protocol can be useful: just adding __setitem__ from the 
mutable sequence protocol allowed us to leverage a ready-to-use function 
from the standard library: random.shuffle. Being aware of existing 
protocols lets us make the most of the rich Python standard library.

Alex Martelli then introduced the term “goose typing” to describe a new 
style of Python programming. With “goose typing,” ABCs are used to make 
interfaces explicit and classes may claim to implement an interface by 
subclassing an ABC or by registering with it, without requiring the strong
and static link of an inheritance relationship.

The FrenchDeck2 example made clear the main drawbacks and advantages of 
explicit ABCs. Inheriting from abc.MutableSequence forced us to implement
two methods we did not really need: insert and __delitem__. On the other 
hand, even a Python newbie can look at FrenchDeck2 and see that it’s a 
mutable sequence. And, as bonus, we inherited 11 ready-to-use methods from
abc.MutableSequence (five indirectly from abc.Sequence).

After a panoramic view of existing ABCs from collections.abc in Figure 
11-3, we wrote an ABC from scratch. Doug Hellmann, creator of the cool 
PyMOTW.com (Python Module of the Week) explains the motivation:

By defining an abstract base class, a common API can be established for a
set of subclasses. This capability is especially useful in situations 
where someone less familiar with the source for an application is going to
provide plug-in extensions...

Alex coined the expression “goose typing” and this is the first time ever
it appears in a book! 

Putting the Tombola ABC to work, we created three concrete subclasses: two
inheriting from Tombola, the other a virtual subclass registered with it,
all passing the same suite of tests.

In concluding the chapter, we mentioned how several built-in types are 
registered to ABCs in the collections.abc module so you can ask 
isinstance(memoryview, abc.Sequence) and get True, even if memoryview does
not inherit from abc.Sequence. And finally we went over the 
__subclasshook__ magic, which lets an ABC recognize any unregistered class
as a subclass, as long as it passes a test that can be as simple or as 
complex as you like. The examples in the standard library merely check for
method names.

To sum up, I’d like to restate Alex Martelli’s admonition that we should 
refrain from creating our own ABCs, except when we are building 
userextensible frameworks — which most of the time we are not. On a daily 
basis, our contact with ABCs should be subclassing or registering classes
with existing ABCs. Less often than subclassing or registering, we might 
use ABCs for isinstance checks. And even more rarely—if ever—we find 
occasion to write a new ABC from scratch.

After 15 years of Python, the first abstract class I ever wrote that is 
not a didactic example was the Board class of the Pingo project. The 
drivers that support different single board computers and controllers are
subclasses of Board, thus sharing the same interface. In reality, although
conceived and implemented as an abstract class, the pingo.Board class does
not subclass abc.ABC as I write this. I intend to make Board an explicit 
ABC eventually—but there are more important things to do in the project.

Here is a fitting quote to end this chapter:
Although ABCs facilitate type checking, it’s not something that you should
overuse in a program. At its heart, Python is a dynamic language that 
gives you great flexibility. Trying to enforce type constraints everywhere
tends to result in code that is more complicated than it needs to be. You
should embrace Python’s flexibility
—David Beazley and Brian Jones, Python Cookbook

Or, as technical reviewer Leonardo Rochael wrote: “If you feel tempted to
create a custom ABC, please first try to solve your problem through 
regular duck-typing.”
