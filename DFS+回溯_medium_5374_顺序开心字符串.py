class Solution:
    # def getHappyString(self, n: int, k: int) -> str:
    def getHappyString(self, n, k):
        def dfs(t, n, arr):
            if len(arr) == n:
                data.append(''.join(arr))
                return
            
            for ele in ['a', 'b', 'c']:
                if not arr or ele != arr[-1]:  # 满足 'Happy' 条件
                    arr.append(ele)
                    dfs(t+1, n, arr)
                    arr.pop()  # 回溯

        data = []
        dfs(0, n, [])
        return data[k-1] if k <= len(data) else ""

res = Solution().getHappyString(1, 3)
print(res)
