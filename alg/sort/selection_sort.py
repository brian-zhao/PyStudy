import time


def find_smallest(arr: list) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


start = time.time()
print(selection_sort([5, 3, 6, 2, 10]))
end = time.time()
print(f"Total time to run this program is {end - start}, {time.process_time()}")
