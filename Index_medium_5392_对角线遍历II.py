# # 暴力超时
# class Solution:
#     # def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#     def findDiagonalOrder(self, nums):
#         max_len = max(len(_) for _ in nums)
#         for i in range(len(nums)):
#             if len(nums[i]) != max_len:
#                 nums[i] = nums[i] + [float("inf")] * (max_len - len(nums[i]))
#         res, row, column = [], len(nums), len(nums[0])
#         # for one in nums:
#         #     print(one)
#         for i in range(row):  # 上三角
#             j = 0
#             while 0<=i and j<column:
#                 if  nums[i][j] != float("inf"):
#                     res.append(nums[i][j])
#                 i -= 1
#                 j += 1
#         for j in range(1, column):
#             i = row - 1
#             while 0<=i and j<column:
#                 if  nums[i][j] != float("inf"):
#                     res.append(nums[i][j])
#                 i -= 1
#                 j += 1
#         return res


# # 时刻调整nums[i] 的大小，较为费时，但能AC
# class Solution:
#     # def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#     def findDiagonalOrder(self, nums):
#         from collections import deque
#         for i in range(len(nums)):
#             mid = deque()
#             mid.extend(nums[i])
#             nums[i] = mid
#         res = []
#         key = True
#         while nums:
#             if key:
#                 i = 0
#                 while i < len(nums):
#                     for j in range(i, -1, -1):
#                         res.append(nums[j].popleft())
#                         if not nums[j]:
#                             del nums[j]
#                             i -= 1
#                     i += 1
#                 key = False
#             i = len(nums)-1
#             while i >= 0:
#                 res.append(nums[i].popleft())
#                 if not nums[i]:
#                     del nums[i]
#                 i -= 1
#         return res


# 巧妙解法：nums[i][j] 必然在第（i + j）次斜线的结果中。i 越小，结果越靠后。
class Solution:
    # def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    def findDiagonalOrder(self, nums):
        sub_result = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j >= len(sub_result):
                    sub_result.append([])
                sub_result[i + j].append(nums[i][j])
                
        result = []
        for sub in sub_result:
            result += sub[::-1]
        return result


nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
res = Solution().findDiagonalOrder(nums)
print(res)

# import collections
# arr = collections.deque()
# arr.extend([1, 2, 3])
# print(arr.popleft())
# print(arr.popleft())
# print(arr.popleft())
# if not arr:
#     print(True)