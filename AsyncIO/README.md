# Async IO
* **Asynchronous IO (async IO)**: a language-agnostic paradigm (model) that has implementations across a host of programming languages.
* **async/await**: two new Python keywords that are used to define coroutines.
* **asyncio**: the Python package that provides a foundation and API for running and managing coroutines.

concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). 
Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency. 
The Python standard library has offered longstanding support for both of these through its multiprocessing, threading, and concurrent.futures packages.


## The Rules of Async IO

* The syntax async def introduces either a **native coroutine** or an **asynchronous generator**. The expressions async with and async for are also valid, and you’ll see them later on.
* The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”

```Python
async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r
```

```Python
async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # OK - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y
```

* @asyncio.coroutine. The result is a generator-based coroutine. This construction has been outdated since the async/await syntax was put in place in Python 3.5.

* These two coroutines are essentially equivalent (both are awaitable), but the first is generator-based, while the second is a native coroutine:
```Python
import asyncio

@asyncio.coroutine
def py34_coro():
    """Generator-based coroutine, older syntax"""
    yield from stuff()

async def py35_coro():
    """Native coroutine, modern syntax"""
    await stuff()
```