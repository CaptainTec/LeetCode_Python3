# class Solution:
#     # def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
#     def constrainedSubsetSum(self, nums, k):
#         key = True  # 若全为 小于等于0的数, 返回最大值
#         for one in nums:
#             if one > 0:
#                 key = False
#                 break
#         if key:    
#             return max(nums)

#         dp = [0] * (len(nums) + 1)
#         i = 0
#         while i < len(nums):
#             if nums[i] >= 0:
#                 dp[i+1] += dp[i] + nums[i]
#                 i += 1
#             else:
#                 mid = []
#                 j = i
#                 while j < len(nums) and nums[j] < 0:
#                     mid.append(nums[j])
#                     j += 1
#                 if len(mid) < k:  # 全部去掉
#                     dp[j] = dp[i]
#                     # for index in range(i, j):
#                     #     dp[index+1] = dp[index]
#                 else:
#                     mid = sorted(mid)
#                     total = sum(mid[k-1:])
#                     print(mid)
#                     print(total)
#                     if  dp[i] + total > 0:
#                         dp[j] = dp[i] + total
#                 i = j
#         print([0] + nums)
#         print(dp)
#         return max(dp)


class Solution:
    def constrainedSubsetSum(self, nums, k):
        dp = nums[:]
        # print(dp)
        dp[0] = nums[0]
        res = nums[0]
        s = [(nums[0], 0)]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], s[0][0] + nums[i])
            while s and s[-1][0] <= dp[i]:
                s.pop()
            s.append((dp[i], i))
            print(dp, s)
            if s[0][1] <= i - k:
                s.pop(0)
            res = max(res, dp[i])
        return res


nums = [10,2,-10,5,20]
# nums = [-1, -2, -3]
# nums = [10,-2,-10,-5,20]
# nums = [-5266,4019,7336,-3681,-5767]
# k = 2
# res = Solution().constrainedSubsetSum(nums, k)
# print(res) 

print(9//10)
