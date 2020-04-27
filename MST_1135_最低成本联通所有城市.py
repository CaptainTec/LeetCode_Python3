class Solution:
    # def minimumCost(self, N: int, connections: List[List[int]]) -> int:
    def minimumCost(self, N, connections):
        from collections import defaultdict
        import heapq  # 优先队列，即 堆
        graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for x, y, c in connections:
            graph[x][y] = min(c, graph[x][y])
            graph[y][x] = min(c, graph[y][x])
        # print(graph)
        heap = [[0, 1]]  # 从节点1开始找
        visited = set()
        res = 0
        while heap:
            c, y = heapq.heappop(heap)
            print(c, y)
            if y in visited: continue
            res += c
            visited.add(y)
            if len(visited) == N:
                return res
            for nxt, c in graph[y].items():
                heapq.heappush(heap, [c, nxt])  # 将 [c, nxt] 压入堆heap中
        return -1

from collections import 
N = 3
c = [[1,2,5],[1,3,6],[2,3,1]]
res = Solution().minimumCost(N, c)
print(res)

