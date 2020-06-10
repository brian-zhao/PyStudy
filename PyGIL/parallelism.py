import os
import sys
import time


def parallelism():
    nums = [1 for _ in range(100000000)]
    chunk_size = len(nums) // 10
    readers = []

    while nums:
        chunk, nums = nums[:chunk_size], nums[chunk_size:]
        reader, writer = os.pipe()
        if os.fork():
            readers.append(reader)  # Parent.
        else:
            # Child process.
            subtotal = 0

            # Intentionally slow code.
            for i in chunk:
                subtotal += i

            print('subtotal %d' % subtotal)

            # Send result to parent, and quit.
            os.write(writer, str(subtotal).encode())
            sys.exit(0)

    start = time.time()
    # Parent.
    total = 0
    for reader in readers:
        subtotal = int(os.read(reader, 1000).decode())
        total += subtotal

    print("Total: %d" % total)
    print('%.2f seconds' % (time.time() - start))


if __name__ == "__main__":
    parallelism()