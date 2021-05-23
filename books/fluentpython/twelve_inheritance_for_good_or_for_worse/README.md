We started our coverage of inheritance explaining the problem with 
subclassing built-in types: their native methods implemented in C do not 
call overridden methods in subclasses, except in very few special cases.
That’s why, when we need a custom list, dict, or str type, it’s easier to
subclass UserList, UserDict, or UserString—all defined in the collections
module, which actually wraps the built-in types and delegate operations to
them—three examples of favoring composition over inheritance in the 
standard library. If the desired behavior is very different from what the
built-ins offer, it may be easier to subclass the appropriate ABC from 
collections.abc and write your own implementation.

The rest of the chapter was devoted to the double-edged sword of multiple
inheritance. First we saw how the method resolution order, encoded in the
__mro__ class attribute, addresses the problem of potential naming 
conflicts in inherited methods. We also saw how the super() built-in 
follows the __mro__ to call a method on a superclass. We then studied how
multiple inheritance is used in the Tkinter GUI toolkit that comes with 
the Python standard library. Tkinter is not an example of current best 
practices, so we discussed some ways of coping with multiple inheritance,
including careful use of mixin classes and avoiding multiple inheritance 
altogether by using composition instead. After considering how multiple 
inheritance is abused in Tkinter, we wrapped up by studying the core parts
of the Django class-based views hierarchy, which I consider a better 
example of mixin usage.

Lennart Regebro—a very experienced Pythonista and one of this book’s 
technical reviewers—finds the design of Django’s mixin views hierarchy 
confusing. But he also wrote:
The dangers and badness of multiple inheritance are greatly overblown. 
I’ve actually never had a real big problem with it.
In the end, each of us may have different opinions about how to use 
multiple inheritance, or whether to use it at all in our own projects. But
often we don’t have a choice: the frameworks we must use impose their own
choices.
