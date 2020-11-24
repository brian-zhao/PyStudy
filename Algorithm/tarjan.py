from typing import List


class Solution:
    def criticalConnections(self,
                            n: int,
                            connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        ans = []
        dfn = [0 for _ in range(n)]
        low = [0 for _ in range(n)]

        def tarjan(u, parent, t):
            nonlocal ans
            dfn[u] = t
            low[u] = t
            for v in graph[u]:
                if v != parent:
                    if not dfn[v]:
                        tarjan(v, u, t + 1)
                        if low[v] > dfn[u]:
                            ans.append([u, v])
                    low[u] = min(low[u], low[v])
        tarjan(0, -1, 1)

        return ans