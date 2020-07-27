# Lists and Tuples

## Differences

1. Lists are dynamic arrays; they are mutable and allow for resizing (changing the number of elements that are held).
2. Tuples are static arrays; they are immutable, and the data within them cannot be changed once they have been created.
3. Tuples are cached by the Python runtime, which means that we don’t need to talk to the kernel to reserve memory every time we want to use one.

## What to use for each use case?
1. First 20 prime numbers (tuple - data is static and wont change.)
2. Names of programming languages (list - the data is constantly growing with DSLs.)
3. A person’s age, weight, and height (list - the data will need to change over time)
4. A person’s birthday and birthplace (tuple - this data will remain the same)
5. The result of a particular game of pool (tuple - the data has static results)
6. The results of a continuing series of pool games (list - the data will continue to grow)

## List as DYNAMIC Arrays
Interestingly, when you append data to a list, python will overallocate additional space to that list, assuming more appends are coming. 
This is important because it effectively avoids expensive memory copies by assuming additional appends.

## Tuples as STATIC Arrays
Instantiating a list can be 5.1x slower than instantiating a tuple—which can add up quite quickly if this is done in a fast loop!
This is due to Tuples being cached, reducing a trip to the operating system on instantiation of a new tuple, when an old tuple has been garbage collected.

## TLDR
Lists and tuples are fast and low-overhead objects to use when your data already has an intrinsic ordering to it. This intrinsic ordering allows you to sidestep the search problem in these structures: if the ordering is known beforehand, then lookups are O(1), avoiding an expensive O(n) linear search. While lists can be resized, you must take care to properly understand how much overallocation is happening to ensure that the dataset can still fit in memory. On the other hand, tuples can be created quickly and without the added overhead of lists, at the cost of not being modifiable.
