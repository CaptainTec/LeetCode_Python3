"""
给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），
请编写一个函数来计算无向图中连通分量的数目。

示例 1:

输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

输出: 2
"""

# 方法一：BFS
class Solution(object):
    def countComponents(self, n, edges):
        import collections
        dic = collections.defaultdict(list)  # 用value默认为list的字典构图，时间复杂度最差情况为O(N^2)
        for e in edges:
            dic[e[0]].append(e[1])
            dic[e[1]].append(e[0])
            
        visited = set()
        res = 0
        # BFS整个图，遍历时间复杂度为O(2N),遍历所有无论visited或没visited的node一次，每个node再被初次visited一次。
        for i in range(n):
            if i not in visited:
                res += 1
                q = [i]
                visited.add(i)
                while q:  # 每一次完整的BFS代表着一个连通分量的完全遍历，res += 1
                    now = q.pop(0)
                    for j in dic[now]:
                        if j not in visited:
                            visited.add(j)
                            q.append(j)
        return res  # 遍历结束输出res即为所求


# DFS
class Solution2(object):
    def countComponents(self, n, edges):
        
        def dfs(node):
            if node in dic:
                for another_node in dic[node]:
                    if another_node not in visited:
                        visited.add(another_node)
                        dfs(another_node)

        import collections
        dic = collections.defaultdict(list)  # 用value默认为list的字典构图，时间复杂度最差情况为O(N^2)
        for e in edges:
            dic[e[0]].append(e[1])
            dic[e[1]].append(e[0])
            
        visited = set()
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1  # 要在dfs外部统计连通分量
                visited.add(i)
                dfs(i)
        return res  # 遍历结束输出res即为所求


# Union Find
class Solution3:
    def countComponents(self, n, edges):
        # Union find
        def find(x):
            # 初始化：各自成树
            dic.setdefault(x, x)  # 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
            if x != dic[x]:
                dic[x] = find(dic[x])
            return dic[x]
        def union(a, b):
            a_root = find(a)
            b_root = find(b)
            dic[b_root] = a_root  # 根据边，合并树
        
        
        dic = {}
        for a, b in edges:
            union(a, b)

        res = set()
        for i in range(n):
            res.add(find(i))
        return len(res)