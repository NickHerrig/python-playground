# Chapter 3 Dictionaries and Sets

Dictionaries are a keystone of Python. Beyond the basic dict, the standard 
library offers handy, ready-to-use specialized mappings like defaultdict, 
OrderedDict, ChainMap, and Counter, all defined in the collections module. 
The same module also provides the easy-to-extend UserDict class.

Two powerful methods available in most mappings are setdefault and update. 
The setdefault method is used to update items holding mutable values, for 
example, in a dict of list values, to avoid redundant searches for the same 
key. The update method allows bulk insertion or overwriting of items from 
any other mapping, from iterables providing (key, value) pairs and from 
keyword arguments. Mapping constructors also use update internally, allowing
instances to be initialized from map‐ pings, iterables, or keyword arguments.

A clever hook in the mapping API is the __missing__ method, which lets you 
customize what happens when a key is not found.

The collections.abc module provides the Mapping and MutableMapping abstract 
base classes for reference and type checking. The little-known MappingProxyType
from the types module creates immutable mappings. 
There are also ABCs for Set and MutableSet.

The hash table implementation underlying dict and set is extremely fast. 
Understanding its logic explains why items are apparently unordered and 
may even be reordered behind our backs. There is a price to pay for all 
this speed, and the price is in memory.
