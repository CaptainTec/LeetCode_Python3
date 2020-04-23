"""
如果要求是恰好装满背包的话，那么dp[0] 初始化为0，其余初始化为 负无穷。

如果没有要求必须把背包装满，只是希望所装的物品价值尽可能的大，则dp初始化为全0
"""

# # 01背包
# def solve3(w,cost,V):
#     """
#     type: w 物品价值
#     type: cost 物品体积
#     type: V 背包体积
#     """
#     dp = [0] * (V+1)
#     for i in range(len(w)):
#         for j in range(V, -1, -1):  # 01背包是逆序
#             if j >= cost[i]:
#                 dp[j] = max(dp[j], dp[j-cost[i]]+w[i])
#         print("01背包-前", i+1, "件物品", dp)
#     return dp[-1]

# if __name__ == '__main__':
#     w = [1,2,5,10]   # 物品价值
#     cost = [1,2,3,4]  # 物品体积
#     V = 9  # 背包容量
#     # n = 3
#     result = solve3(w,cost,V)
#     print(result)







# # 完全背包
# def solve3(w,cost,V):
#     """
#     type: w 物品价值
#     type: cost 物品体积
#     type: V 背包体积
#     """
#     dp = [0] * (V+1)
#     for i in range(len(w)):
#         for j in range(cost[i],V+1):  # 完全背包，升序遍历
#             dp[j] = max(dp[j], dp[j-cost[i]]+w[i])
#         print("完全背包-前", i+1, "件物品", dp)
#     return dp[-1]

# if __name__ == '__main__':
#     w = [10,2,5,10]   # 物品价值
#     cost = [10,2,3,4]  # 物品体积
#     V = 9  # 背包容量
#     # n = 3
#     result = solve3(w,cost,V)
#     print(result)


# 完全背包 -- 拼凑钱币(物品的体积和价值相等)
def solve3(w,cost,V):
    """
    type: w 物品价值
    type: cost 物品体积
    type: V 背包体积
    """
    dp = [1] + [0] * (V)
    for i in range(len(w)):
        for j in range(cost[i],V+1):  # 完全背包，升序遍历
            dp[j] += dp[j-cost[i]]
        print("完全背包-前", i+1, "件物品", dp)
    return dp[-1]

if __name__ == '__main__':
    w = [1,2,5,10]   # 物品价值
    cost = [1,2,5,10]  # 物品体积
    V = 9  # 背包容量
    # n = 3
    result = solve3(w,cost,V)
    print(result)
    