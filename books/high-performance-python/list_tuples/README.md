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

## List overallocation of memory
Interestingly, when you append data to a list, python will overallocate additional space to that list, assuming more appends are coming. 
This is important because it effectively avoids expensive memory copies by assuming additional appends.

