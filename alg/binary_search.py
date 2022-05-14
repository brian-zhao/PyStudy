# Binary Search
from typing import Optional


def binary_search(a_list: list, item: int) -> Optional[int]:
    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = a_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
    return None


a_list = [1, 3, 5, 7, 9]
assert binary_search(a_list, 5) == 2
assert binary_search(a_list, 10) is None
