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


## coroutines as generators
* Coroutines are repurposed generators that take advantage of the peculiarities of generator methods.
* Old generator-based coroutines use yield from to wait for a coroutine result. Modern Python syntax in native coroutines simply replaces yield from with await as the means of waiting on a coroutine result. The await is analogous to yield from, and it often helps to think of it as such.
* The use of await is a signal that marks a break point. It lets a coroutine temporarily suspend execution and permits the program to come back to it later.

## Other Features
* **asynchronous generator**
```python
>>> async def mygen(u: int = 10):
...     """Yield powers of 2."""
...     i = 0
...     while i < u:
...         yield 2 ** i
...         i += 1
...         await asyncio.sleep(0.1)
```

* **asynchronous comprehension**
```python
>>> async def main():
...     # This does *not* introduce concurrent execution
...     # It is meant to show syntax only
...     g = [i async for i in mygen()]
...     f = [j async for j in mygen() if not (j // 3 % 5)]
...     return g, f
...
>>> g, f = asyncio.run(main())
>>> g
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
>>> f
[1, 2, 16, 32, 256, 512]
```

This is a crucial distinction: neither asynchronous generators nor comprehensions make the iteration concurrent.


## The Event loop and asyncio.run()
```python
asyncio.run()
```
same as
```python
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
```
1: Coroutines don’t do much on their own until they are tied to the event loop.
2: By default, an async IO event loop runs in a single thread and on a single CPU core.
3: Event loops are pluggable. That is, you could, if you really wanted, write your own event loop implementation and have it run tasks just the same.


## Asynchronous Requests
1. Read a sequence of URLs from a local file, urls.txt.

2. Send GET requests for the URLs and decode the resulting content. If this fails, stop there for a URL.

3. Search for the URLs within href tags in the HTML of the responses.

4. Write the results to foundurls.txt.

5. Do all of the above as asynchronously and concurrently as possible. (Use aiohttp for the requests, and aiofiles for the file-appends. These are two primary examples of IO that are well-suited for the async IO model.)

## Odds and others
* You can use create_task() to schedule the execution of a coroutine object, followed by asyncio.run():
```python
>>> import asyncio

>>> async def coro(seq) -> list:
...     """'IO' wait time is proportional to the max element."""
...     await asyncio.sleep(max(seq))
...     return list(reversed(seq))
...
>>> async def main():
...     # This is a bit redundant in the case of one task
...     # We could use `await coro([3, 2, 1])` on its own
...     t = asyncio.create_task(coro([3, 2, 1]))  # Python 3.7+
...     await t
...     print(f't: type {type(t)}')
...     print(f't done: {t.done()}')
...
>>> t = asyncio.run(main())
t: type <class '_asyncio.Task'>
t done: True
```

* asyncio.gather()
```python
>>> import time
>>> async def main():
...     t = asyncio.create_task(coro([3, 2, 1]))
...     t2 = asyncio.create_task(coro([10, 5, 0]))  # Python 3.7+
...     print('Start:', time.strftime('%X'))
...     a = await asyncio.gather(t, t2)
...     print('End:', time.strftime('%X'))  # Should be 10 seconds
...     print(f'Both tasks done: {all((t.done(), t2.done()))}')
...     return a
...
>>> a = asyncio.run(main())
Start: 16:20:11
End: 16:20:21
Both tasks done: True
>>> a
[[1, 2, 3], [0, 5, 10]]
```

* You probably noticed that gather() waits on the entire result set of the Futures or coroutines that you pass it. Alternatively, you can loop over asyncio.as_completed() to get tasks as they are completed
```python
>>> async def main():
...     t = asyncio.create_task(coro([3, 2, 1]))
...     t2 = asyncio.create_task(coro([10, 5, 0]))
...     print('Start:', time.strftime('%X'))
...     for res in asyncio.as_completed((t, t2)):
...         compl = await res
...         print(f'res: {compl} completed at {time.strftime("%X")}')
...     print('End:', time.strftime('%X'))
...     print(f'Both tasks done: {all((t.done(), t2.done()))}')
...
>>> a = asyncio.run(main())
Start: 09:49:07
res: [1, 2, 3] completed at 09:49:10
res: [0, 5, 10] completed at 09:49:17
End: 09:49:17
Both tasks done: True
```


##Conclusion
You’re now equipped to use async/await and the libraries built off of it. Here’s a recap of what you’ve covered:

* Asynchronous IO as a language-agnostic model and a way to effect concurrency by letting coroutines indirectly communicate with each other

* The specifics of Python’s new async and await keywords, used to mark and define coroutines

* asyncio, the Python package that provides the API to run and manage coroutines