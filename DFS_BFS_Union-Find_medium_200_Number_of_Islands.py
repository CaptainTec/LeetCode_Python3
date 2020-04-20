# # DFS
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0

#         def dfs(i, j):
#             visit[i][j] = 1

#             for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
#                 if 0<=i+a<m and 0<=j+b<n and not visit[i+a][j+b] and grid[i+a][j+b] == '1':
#                     dfs(i+a, j+b)
        
#         m, n = len(grid), len(grid[0])  # row column
#         visit = [[0]*n for _ in range(m)]
#         cnt = 0
#         for i in range(m):
#             for j in range(n):
#                 if not visit[i][j] and grid[i][j] == '1':
#                     cnt += 1
#                     dfs(i, j)
#         return cnt

# BFS
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0

#         m, n = len(grid), len(grid[0])  # row column
#         visit = [[0]*n for _ in range(m)]
#         cnt = 0
#         for i in range(m):
#             for j in range(n):
#                 if not visit[i][j] and grid[i][j] == '1':
#                     cnt += 1
#                     queue = [(i, j)]
#                     visit[i][j] = 1  # 应该尽早的标记
#                     while queue:
#                         k, t = queue.pop(0)
#                         # visit[k][t] = 1  # 访问标记加在这里会超时，应该尽早的标记，相当于添加约束
#                         for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
#                             if 0<=k+a<m and 0<=t+b<n and not visit[k+a][t+b] and grid[k+a][t+b] == '1':
#                                 queue.append((k+a, t+b))
#                                 visit[k+a][t+b] = 1  # 应该尽早的标记，相当于添加约束
#         return cnt


# Union Find
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])  # row, column
        self.count = 0
        self.parent = [-1] * (m * n)
        # self.rank = [0] * (m * n)  # rank的作用是增加树的宽度，以降低树的深度
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            # if self.rank[rootx] < self.rank[rooty]:
            #     rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            # if self.rank[rootx] == self.rank[rooty]:  # rank的作用是降低树的深度
            #     self.rank[rootx] += 1
            self.count -= 1
    
    def getCount(self):
        return self.count

class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        uf = UnionFind(grid)
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)
        
        return uf.getCount()
