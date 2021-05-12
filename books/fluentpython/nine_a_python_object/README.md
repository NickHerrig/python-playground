The aim of this chapter was to demonstrate the use of special methods and
conventions in the construction of a well-behaved Pythonic class.

Is vector2d_v3.py (Example 9-9) more Pythonic than vector2d_v0.py 
(Example 9-2)? The Vector2d class in vector2d_v3.py certainly exhibits 
more Python features. But whether the first or the last Vector2d 
implementation is more idiomatic depends on the context where it would be
used. 

Tim Peter’s Zen of Python says:
  - Simple is better than complex.

A Pythonic object should be as simple as the requirements allow—and not a
parade of language features. But my goal in expanding the Vector2d code 
was to provide context for discussing Python special methods and coding 
conventions. If you look back at Table 1-1, the several listings in this
chapter demonstrated:

- All string/bytes representation methods: __repr__, __str__, __format__,
and __bytes__.

- Several methods for converting an object to a number: __abs__, __bool__,
__hash__.

- The __eq__ operator, to test bytes conversion and to enable hashing 
(along with __hash__).

While supporting conversion to bytes we also implemented an alternative
constructor, Vector2d.frombytes(), which provided the context for 
discussing the decorators @classmethod (very handy) and @staticmethod 
(not so useful, module-level functions are simpler). The frombytes method
was inspired by it’s namesake in the array.array class.


We saw that the Format Specification Mini-Language is extensible by 
implementing a __format__ method that does some minimal parsing of 
format_spec provided to the format(obj, format_spec) built-in or within 
replacement fields '{:«for mat_spec»}' in strings used with the str.format
method.

In preparation to make Vector2d instances hashable, we made an effort to
make them immutable, at least preventing accidental changes by coding the
x and y attributes as private, and exposing them as read-only properties.
We then implemented __hash__ using the recommended technique of xoring the
hashes of the instance attributes.

We then discussed the memory savings and the caveats of declaring a 
__slots__ attribute in Vector2d. Because using __slots__ is somewhat 
tricky, it really makes sense only when handling a very large number of 
instances, think millions of instances, not just thousands.

The last topic we covered was the overriding of a class attribute accessed
via the instances (e.g., self.typecode). We did that first by creating an
instance attribute, and then by subclassing and overwriting at the class
level.

Throughout the chapter, I mentioned how design choices in the examples
were informed by studying the API of standard Python objects. If this 
chapter can be summarized in one sentence, this is it:

To build Pythonic objects, observe how real Python objects behave.
- Ancient Chinese proverb
