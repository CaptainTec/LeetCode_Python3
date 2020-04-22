# BFS
# class Solution:
#     # def rightSideView(self, root: TreeNode) -> List[int]:
#     def rightSideView(self, root):
#         """
#         BFS 右孩子先进队的话，则每层的第一个节点即为该层最右的节点
#         酱紫不用统计每层节点数量，只通过层次变化来找每层第一个节点
#         """
#         import collections
#         if not root: return []
        
#         res = []
#         queue = collections.deque([(root, 1)])  # (node, depth)
#         layer = 0
#         while queue:
#             top = queue.popleft(0)
#             if top[1] != layer:  # this layer's first node
#                 res.append(top[0].val)
#                 layer += 1
#             if top[0].right:  # right child first in
#                 queue.append((top[0].right, top[1]+1))
#             if top[0].left:
#                 queue.append((top[0].left, top[1]+1))
#         return res


# DFS
class Solution:
    def rightSideView(self, root):

        def dfs(node, depth):
            if node:
                if depth == len(res):  # 如果当前节点所在的深度还没有出现在res里，说明该节点是该层第一个被访问的，需要加入res中
                    res.append(node.val)
                dfs(node.right, depth+1)
                dfs(node.left, depth+1)

        res = []
        dfs(root, 0)
        return res

        