"""
假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k​​​​​​​ 个更新的操作。

其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，
你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。

请你返回 k 次操作后的数组。

示例:

输入: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
输出: [-2,0,3,5,3]
解释:

初始状态:
[0,0,0,0,0]

进行了操作 [1,3,2] 后的状态:
[0,2,2,2,0]

进行了操作 [2,4,3] 后的状态:
[0,2,5,5,3]

进行了操作 [0,2,-2] 后的状态:
[-2,0,3,5,3]

"""

# Force - O(n*k)
# class Solution:
#     def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
#         res = [0] * length
#         data_dict = {}  # {(startIndex, endIndex): inc, ... }, 这么做是为了合并相同区间的操作
#         for triple in updates:
#             if (triple[0], triple[1]) in data_dict:
#                 data_dict[(triple[0], triple[1])] += triple[2]
#             else:
#                 data_dict[(triple[0], triple[1])] = triple[2]

#         for k, v in data_dict.items():
#             for i in range(k[0], k[1]+1):
#                 res[i] += v
#         return res


# 差分数组 - O(n+k)
class Solution:
    # def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    def getModifiedArray(self, length, updates):
        res = [0] * length
        for triple in updates:
            res[triple[0]] += triple[2] 
            if triple[1] < length - 1:
                res[triple[1]+1] -= triple[2] 
        for i in range(1, length):
            res[i] += res[i-1]
        return res


"""
更多思考
此问题的一个拓展是如何将这样的更新操作应用在一个初始元素 不 是一样的数组里。

这种情况下，第二种方法需要额外的 O(n) 的空间来保存初始的值。

另一种不需要额外空间的方法，但需要对数组做一次额外的线性遍历，这个想法跟上面部分和的想法正好相反，
比方说将数组 [2,3,10,5] 转变成 [2,1,7,−5] 作为 arrarr 数组的初始值，然后后面操作照常。

即将上面 3-2， 10-3， 5-10 的值更新原数组的值。
"""
