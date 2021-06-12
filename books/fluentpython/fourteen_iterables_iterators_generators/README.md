Iteration is so deeply embedded in the language that I like to say that 
Python groks iterators. The integration of the Iterator pattern in the 
semantics of Python is a prime example of how design patterns are not 
equally applicable in all programming languages. In Python, a classic 
iterator implemented “by hand” as in Example 14-4 has no practical use, 
except as a didactic example.

In this chapter, we built a few versions of a class to iterate over 
individual words in text files that may be very long. Thanks to the use of
generators, the successive refactorings of the Sentence class become 
shorter and easier to read—when you know how they work.

We then coded a generator of arithmetic progressions and showed how to 
leverage the itertools module to make it simpler. An overview of 24 
general-purpose generator functions in the standard library followed.

Following that, we looked at the iter built-in function: first, to see how
it returns an iterator when called as iter(o), and then to study how it 
builds an iterator from any function when called as iter(func, sentinel).

For practical context, I described the implementation of a database 
conversion utility using generator functions to decouple the reading to 
the writing logic, enabling efficient handling of large datasets and 
making it easy to support more than one data input format.

Also mentioned in this chapter were the yield from syntax, new in 
Python 3.3, and coroutines. Both topics were just introduced here; they 
get more coverage later in the book.
