class Solution:
    def findMinFibonacciNumbers(self, k):
        import sys
        sys.setrecursionlimit(1000000) #这里设置大一些
        def dfs(value, time):
            if value == 0:
                res.append(time)
                return 
            if not res:
                for one in data:
                    if value >= one:
                        dfs(value-one, time+1)

        data = set([1])
        a, b = 1, 1
        while b < k:
            a, b = b, a+b
            data.add(b)
        data = sorted(list(data), reverse=True)

        # print(len(data))
        # print(data)
        res = []
        dfs(k, 0)
        # print(res)
        return res[0]
        
        

k = 9083494
k = 19
k = 10
res = Solution().findMinFibonacciNumbers(k)
print(res)