import multiprocessing.pool
from absl import app

INPUT_COUNT = 100
WORKER_COUNT = 10

def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

def main(argv):
    data = [30] * INPUT_COUNT
    pool = multiprocessing.pool.ThreadPool(WORKER_COUNT)
    print(pool.map(fib, data))

if __name__ == '__main__':
    app.run(main)
