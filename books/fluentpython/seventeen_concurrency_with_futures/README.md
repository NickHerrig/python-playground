We started the chapter by comparing two concurrent HTTP clients
with a sequential one, demonstrating significant performance 
gains over the sequential script.

After studying the first example based on concurrent.futures,
we took a closer look at future objects, either instances of 
concurrent.futures.Future, or asyncio.Future, emphasizing what
these classes have in common (their differences will be
emphasized in Chapter 18). We saw how to create futures by 
calling Executor.submit(...), and iterate over completed 
futures with concurrent.futures.as_completed(...).

Next, we saw why Python threads are well suited for I/O-bound 
applications, despite the GIL: every standard library I/O 
function written in C releases the GIL, so while a given thread
is waiting for I/O, the Python scheduler can switch to another
thread. We then discussed the use of multiple processes with 
the concurrent.futures.ProcessPoolExecutor class, to go around
the GIL and use multiple CPU cores to run cryptographic 
algorithms, achieving speedups of more than 100% when using 
four workers.

In the following section, we took a close look at how the 
concurrent.futures.ThreadPoolExecutor works, with a didactic 
example launching tasks that did nothing for a few seconds, 
except displaying their status with a timestamp.

Next we went back to the flag downloading examples. Enhancing 
them with a progress bar and proper error handling prompted 
further exploration of the future.as_completed generator 
function showing a common pattern: storing futures in a dict to
link further information to them when submitting, so that we 
can use that information when the future comes out of the 
as_completed iterator.

We concluded the coverage of concurrency with threads and 
processes with a brief reminder of the lower-level, but more 
flexible threading and multiprocessing modules, which represent
the traditional way of leveraging threads and processes in 
Python.
