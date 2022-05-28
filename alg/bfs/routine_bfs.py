from collections import deque

graph = {}
graph["wakeup"] = ["exercise", "brush teeth", "pack lunch"]
graph["exercise"] = ["shower"]
graph["shower"] = ["wear cloth"]
graph["brush teeth"] = ["eat breakfast"]
graph["wear cloth"] = []
graph["eat breakfast"] = []
graph["pack lunch"] = []


def routine(
    search_queue: deque,
) -> list:
    result = []
    searched = []
    while search_queue:
        activity = search_queue.popleft()
        if activity not in searched:
            result.append(activity)
            search_queue += graph[activity]

    return result


search_queue = deque()
search_queue += graph["wakeup"]
print(["wakeup"] + routine(search_queue))
