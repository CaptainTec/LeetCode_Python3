# class Solution:
#     def maxScore(self, cardPoints, k):
#         dp = [0] * (k+1)
#         # dp[i] = dp[i-1] + max(num[0], num[-1])
#         from collections import deque
#         queue = deque()
#         queue.extend(cardPoints)
#         # for one in cardPoints:
#         #     deque.append(one)
#         for i in range(1, k+1):
#             if queue[0] >= queue[-1]:
#                 dp[i] = dp[i-1] + queue[0]
#                 queue.popleft()
#             else:
#                 dp[i] = dp[i-1] + queue[-1]
#                 queue.pop()
#         return max(dp[-1], sum(cardPoints[:k]), sum(cardPoints[-k:]))


class Solution:
    def maxScore(self, cardPoints, k):
        if k >= len(cardPoints):
            return sum(cardPoints)
        
        left = cardPoints[:]
        right = cardPoints[:]
        for i in range(1, k):
            left[i] += left[i-1]
        for i in range(2, k+1):
            right[-i] += right[-i+1]
        
        print(cardPoints)
        print(left)
        print(right)
        res = max(left[k-1], right[-k])
        for i in range(k-1):
            res = max(res, left[i] + right[-k+i+1])
        return res



a = [1,2,3,4,5,6,1]
a = [2, 2, 2]
k = 2
# print(a[:1])
res = Solution().maxScore(a, k)
print(res)