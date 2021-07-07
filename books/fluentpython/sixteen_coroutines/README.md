Guido van Rossum wrote there are three different styles of code
you can write using generators:
There’s the traditional “pull” style (iterators),
"push” style (like the averaging example), 
and then there are “tasks” 

Chapter 14 was devoted to iterators; this chapter introduced 
coroutines used in “push style” and also as very simple “tasks”
The taxi processes in the simulation example. Chapter 18 will 
put them to use as asynchronous tasks in concurrent 
programming.

The running average example demonstrated a common use for a 
coroutine: as an accumulator processing items sent to it. We 
saw how a decorator can be applied to prime a coroutine, making
it more convenient to use in some cases. But keep in mind that
priming decorators are not compatible with some uses of 
coroutines. In particular, yield from subgenerator() assumes 
the subgenerator is not primed, and primes it automatically.

Accumulator coroutines can yield back partial results with each
send method call, but they become more useful when they can 
return values, a feature that was added in Python 3.3 with 
PEP 380. We saw how the statement return the_result in a 
generator now raises StopIteration(the_result), allowing the 
caller to retrieve the_result from the value attribute of the 
exception. This is a rather cumbersome way to retrieve 
coroutine results, but it’s handled automatically by the yield from syntax introduced in PEP 380.

The coverage of yield from started with trivial examples using
simple iterables, then moved to an example highlighting the 
three main components of any significant use of yield from: 
 - the delegating generator (defined by the use of yield from in its body), 
 - the subgenerator activated by yield from
 - and the client code that actually drives the whole setup by sending values to the subgenerator through the pass through channel established by yield from in the delegating generator.

This section was wrapped up with a look at the formal 
definition of yield from behavior as described in PEP 380 using
English and Python like pseudocode.

We closed the chapter with the discrete event simulation 
example, showing how generators can be used as an alternative 
to threads and callbacks to support concurrency. Although 
simple, the taxi simulation gives a first glimpse at how 
event-driven frameworks like Tornado and asyncio use a main 
loop to drive coroutines executing concurrent activities with a
single thread of execution. In event-oriented programming with
coroutines, each concurrent activity is carried out by a 
coroutine that repeatedly yields control back to the main loop,
allowing other coroutines to be activated and move forward. 
This is a form of cooperative multitasking: coroutines 
voluntarily and explicitly yield control to the central 
scheduler. In contrast, threads implement preemptive 
multitasking. The scheduler can suspend threads at any time 
even halfway through a statement to give way to other threads.

One final note: this chapter adopted a broad, informal 
definition of a coroutine: a generator function driven by a 
client sending it data through .send(...) calls or yield from.
This broad definition is the one used in PEP 342 — Coroutines 
via Enhanced Generators and in most existing Python books as I
write this. The asyncio library we’ll see in Chapter 18 is 
built on coroutines, but a stricter definition of coroutine is
adopted there: asyncio coroutines are (usually) decorated with
an @asyncio.coroutine decorator, and they are always driven by
yield from, not by calling .send(...) directly on them. Of 
course, asyncio coroutines are driven by next(...) and 
.send(...) under the covers, but in user code we only use 
yield from to make them run.
