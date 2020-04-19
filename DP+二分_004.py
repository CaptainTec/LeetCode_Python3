from collections import deque
class Solution:
    def minJump(self, s):
        mid = 1
        n = len(s)
        dp = [0]*(n-1)+[1]
        st = deque([(1, n-1), (0, n)])  # (step, index)
        print(dp, st, '\n')
        for i in range(n-2, -1, -1):
            if i + s[i] >= n:
                dp[i] = 1
                st = deque([(1, i), (0, n)])
            else:
                x = i+s[i]  # x 表示 当前下标i 和对应的值s[i] 组成的最大下标
                left, right = 0, len(st)-1
                while left+1 < right:
                    mid = (left+right)//2
                    if x >= st[mid][1]:  # x表示的下标 大于 当前mid能到达的下标
                        left = mid
                    else:
                        right = mid
                # print(left, right) 跳出循环时 st[left][1]是小于x的最大值
                dp[i] = min(dp[x], st[left][0]+1) + 1
                while st[0][0]>dp[i]:
                    st.popleft()
                st.appendleft((dp[i], i))  # (step, index)
            print(dp, st)
        return dp[0]


jump = [2, 6, 2, 1, 2, 1, 2, 1, 2, 1]  # 10 个 1
res = Solution().minJump(jump)
print(res)