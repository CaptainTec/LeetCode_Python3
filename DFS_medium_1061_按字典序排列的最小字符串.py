"""
自己写的题解
https://leetcode-cn.com/problems/lexicographically-smallest-equivalent-string/solution/dfs-bfs-bing-cha-ji-3chong-jie-fa-by-captaintec/
"""

# # DFS
# class Solution:
#     # def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
#     def smallestEquivalentString(self, A, B, S):

#         def dfs(ele, res_char, visit, data_dict):
#             res_char = min(res_char, ele)
#             if ele not in visit:
#                 visit.add(ele)
#                 for one in data_dict[ele]:
#                     res_char = min(res_char, dfs(one, res_char, visit, data_dict))  # dfs
#             return res_char

#         import collections
#         data_dict = collections.defaultdict(set)
#         for i in range(len(A)):
#             data_dict[A[i]].add(B[i])
#             data_dict[B[i]].add(A[i])
#         res = ""
#         for ele in S:
#             visit = set()
#             res += dfs(ele, ele, visit, data_dict)
#         return res


# # BFS
# class Solution:
#     # def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
#     def smallestEquivalentString(self, A, B, S):

#         def bfs(ele, visit, data_dict):
#             min_char = ele
#             queue.append(ele)
#             while queue:
#                 top = queue.popleft()
#                 min_char = min(min_char, top)
#                 if top not in visit:
#                     visit.add(top)
#                     for one in data_dict[top]:
#                         queue.append(one)
#             return min_char

#         import collections
#         queue = collections.deque()
#         data_dict = collections.defaultdict(set)
#         for i in range(len(A)):
#             data_dict[A[i]].add(B[i])
#             data_dict[B[i]].add(A[i])    
#         res = ""
#         for ele in S:
#             visit = set()
#             res += bfs(ele, visit, data_dict)
#         return res


# Union-Find
class Solution:
    # def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
    def smallestEquivalentString(self, A, B, S):

        def find(char):
            if char != data_dict[char]:
                data_dict[char] = find(data_dict[char])
            return data_dict[char]

        import collections
        data_dict = collections.defaultdict(str)
        for i in range(len(A)):
            if A[i] not in data_dict and B[i] not in data_dict:
                a = min(A[i], B[i])
                b = max(A[i], B[i])
                data_dict[a] = a
                data_dict[b] = a 
            elif A[i] not in data_dict:
                mid = find(B[i])
                if A[i] > mid:
                    data_dict[A[i]] = mid
                else:
                    data_dict[A[i]] = A[i]
                    data_dict[mid] = A[i]
            elif B[i] not in data_dict:
                mid = find(A[i])
                if B[i] > mid:
                    data_dict[B[i]] = mid
                else:
                    data_dict[B[i]] = B[i]
                    data_dict[mid] = B[i]
            else:  # 都在哈希表中
                mid_a = find(A[i])
                mid_b = find(B[i])
                if mid_a > mid_b:
                    data_dict[mid_a] = mid_b
                else:
                    data_dict[mid_b] = mid_a
            
        res = ""
        for ele in S:
            if ele in data_dict:
                res += find(ele)
            else:
                res += ele
        return res






A = "parker"
B = "morris"
S = "parser"
A = "leetcode"
B = "programs"
S = "sourcecode"
# A = "bcfeaabddgcdaefcbfadggfagfgfedeefbebdbeefbecggcgge"
# B = "feegaacabcfadggfcaabcbadbbecbfdcabgeaegfcagdfggdgg"
# S = "mytnpodxbwxcxcplapgrqjzkfrkizffkbquwqbkxmpqjmxykvb"
# A = "opecenadojbodihfgmpijpfocomhcncicefpohkibjckijghii"
# B = "ndlbhpaeppgekfhnjnmmplmdoifdhbglmedpjgleofgnahglbe"
# S = "ttusuhhrabgsswpaapxoxdanchyccmpjitwwmfioedtbiggfru"
res = Solution().smallestEquivalentString(A, B, S)
print(res)

