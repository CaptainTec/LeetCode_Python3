"""
256. 粉刷房子
假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，
你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。
每个房子粉刷成不同颜色的花费是以一个 n x 3 的矩阵来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，
以此类推。请你计算出粉刷完所有房子最少的花费成本。

注意：

所有花费均为正整数。

示例：

输入: [[17,2,17],[16,16,5],[14,3,19]]
输出: 10
解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
     最少花费: 2 + 5 + 3 = 10。


# 状态转移方程
R[0] = cost[0][0]
B[0] = cost[0][1]
G[0] = cost[0][2]

R[1] = min(B[0], G[0]) + cost[1][0]
B[1] = min(R[0], G[0]) + cost[1][1]
G[1] = min(R[0], B[0]) + cost[1][2]

R[k] = min(B[k-1], G[k-1]) + cost[k][0]
B[k] = min(R[k-1], G[k-1]) + cost[k][1]
G[k] = min(R[k-1], B[k-1]) + cost[k][2]

result = min(R[n-1], B[n-1], G[n-1])
"""


# DP
class Solution:
    # def minCost(self, costs: List[List[int]]) -> int:
    def minCost(self, costs):
        if not costs:  # 特判
            return 0
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1][0], costs[-1][1], costs[-1][2])

sol = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]
print(sol.minCost(costs))
