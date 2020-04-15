"""
方法一：BFS

方法二：DP
"""

# BFS
class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        res = [[float("inf")] * n for _ in range(m)]
        visit = [[0] * n for _ in range(m)]
        queue = []
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    visit[i][j] = 1
                    res[i][j] = 0
                    queue.append([i, j])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:  # BFS
            row, col = queue.pop(0)
            for a, b in directions:
                if 0<= row+a < m and 0 <= col+b < n and not visit[row+a][col+b]:
                    res[row+a][col+b] = res[row][col] + 1
                    visit[row+a][col+b] = 1
                    queue.append([row+a, col+b])
        
        return res


# DP
# class Solution:
#     def updateMatrix(self, matrix):
#         m, n = len(matrix), len(matrix[0])
#         # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
#         dist = [[10**9] * n for _ in range(m)]
#         # 如果 (i, j) 的元素为 0，那么距离为 0
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     dist[i][j] = 0
#         # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
#         for i in range(m):
#             for j in range(n):
#                 if i - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
#                 if j - 1 >= 0:
#                     dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
#         # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
#         for i in range(m - 1, -1, -1):
#             for j in range(n - 1, -1, -1):
#                 if i + 1 < m:
#                     dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
#                 if j + 1 < n:
#                     dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
#         return dist