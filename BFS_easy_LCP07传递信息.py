class Solution:
    def numWays(self, n, relation, k):
        data_dict = {}
        for one in relation:
            if one[0] in data_dict:
                data_dict[one[0]].add(one[1])
            else:
                data_dict[one[0]] = set([one[1]])
        queue, cnt = [], 0
        if 0 not in data_dict:
            return 0
        
        for ele in data_dict[0]:
            queue.append((ele, 1))
        while queue:  # BFS
            top = queue.pop(0)
            if top[1] == k and top[0] == n-1:
                cnt += 1
            if top[1] < k and top[0] in data_dict:
                for ele in data_dict[top[0]]:
                    queue.append((ele, top[1]+1))
        return cnt
                
n = 5
r = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
k = 1

res = Solution().numWays(n, r, k)
print(res)