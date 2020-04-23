class Solution:
    # def minimumLengthEncoding(self, words: List[str]) -> int:
    def minimumLengthEncoding(self, words):
        class Node:
            def __init__(self, l):
                self.l = l # 层数
                self.children = {}
        
        root = Node(0)
        def build(t, w): # 递归构造字典树
            if not w:
                return
            if w[-1] not in t.children:
                t.children[w[-1]] = Node(t.l + 1)
            build(t.children[w[-1]], w[:-1])
        for w in words:
            build(root, w)
        print(root.children)
        ans = [0] # 相当于全局变量，以便在递归中累加

        def vis(t):  # 计算答案
            if len(t.children) == 0: # 是叶子节点
                if t.l > 0:
                    ans[0] += t.l + 1 # 累加
            for c in t.children.values():
                vis(c)  # 递归
        vis(root)
        return ans[0]

w = ["time", "me", "bell"]
res = Solution().minimumLengthEncoding(w)
print(res)
