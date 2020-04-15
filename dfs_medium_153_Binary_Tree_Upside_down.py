# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# 较low的递归 -- 自己写的
# class Solution:
#     def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return None
#         if not root.left and not root.right:
#             return root
        
#         def handle(root):
#             if root.left.left:
#                 new_root, rear = handle(root.left)
#                 rear.left = root.right
#                 rear.right = root

#                 if root.right:  # 如果右孩子存在
#                     root.right.left = None
#                     root.right.right = None
#                 root.left = None
#                 root.right = None
#                 return new_root, root
#             else:
#                 new_root = root.left
#                 new_root.left = root.right
#                 new_root.right = root
#                 if root.right:  # 如果右孩子存在
#                     root.right.left = None
#                     root.right.right = None
#                 root.left = None
#                 root.right = None
#                 return new_root, root
#         r, rear = handle(root)
#         return r


# DFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        #    4     5
        #     \   /
        #       2    
        #      / \ 
        #     3   1
        if root == None: return None
        def dfs(node):
            if not node.left and not node.right: return node
            res = dfs(node.left)
            node.left.right = node
            node.left.left = node.right
            return res
        tempRoot = root # process root particularly.
        root = dfs(root)
        tempRoot.left, tempRoot.right = None, None
        return root

