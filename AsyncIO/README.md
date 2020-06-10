
* **Asynchronous IO (async IO)**: a language-agnostic paradigm (model) that has implementations across a host of programming languages.
* **async/await**: two new Python keywords that are used to define coroutines.
* **asyncio**: the Python package that provides a foundation and API for running and managing coroutines.

concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). 
Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency. 
The Python standard library has offered longstanding support for both of these through its multiprocessing, threading, and concurrent.futures packages.