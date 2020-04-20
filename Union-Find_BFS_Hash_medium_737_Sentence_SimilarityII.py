# # 字典 - O(N + P)
# class Solution:
#     def areSentencesSimilarTwo(self, words1, words2, pairs):
#         """
#         words1, words2: List[str]
#         pairs: List[List[str]]
#         return: bool
#         """
#         len_w1, len_w2 = len(words1), len(words2)
#         if len_w1 != len_w2:
#             return False

#         import collections
#         data_dict = collections.defaultdict(set)
#         for a, b in pairs:
#             data_dict[a].add(b)
#             data_dict[b].add(a)
#         mid_list = []
#         while data_dict:  # 跳出循环时 字典为空
#             mid_set = set()
#             a = data_dict.popitem()  # tuple(str: set(str))
#             queue = [a]
#             while queue:
#                 top = queue.pop(0)
#                 mid_set.add(top[0])
#                 for one in top[1]:
#                     mid_set.add(one)
#                     if one in data_dict:
#                         queue.append((one, data_dict[one]))
#                         data_dict.pop(one)
#             mid_list.append(mid_set)
        
        
#         # 重新对data_dict 字典元素进行赋值
#         for one_set in mid_list:
#             for one in one_set:
#                 data_dict[one] = one_set  # 每个value是对应的相似的整个集合

#         for i in range(len_w1):
#             if words2[i] == words1[i] or words2[i] in data_dict[words1[i]]:
#                 continue
#             else:
#                 return False
#         return True


# # BFS - O(NP)
# class Solution(object):
#     def areSentencesSimilarTwo(self, words1, words2, pairs):
#         if len(words1) != len(words2): return False
#         import collections
#         graph = collections.defaultdict(set)
#         for w1, w2 in pairs:
#             graph[w1].add(w2)
#             graph[w2].add(w1)

#         for w1, w2 in zip(words1, words2):
#             stack, seen = [w1], {w1}
#             # 当while循环正常结束的情况下，才执行else块中的语句
#             while stack:
#                 word = stack.pop()
#                 if word == w2: break  # 当while 块遇到break强制跳出的时候，else 块中的语句不被执行。
#                 for nei in graph[word]:
#                     if nei not in seen:
#                         seen.add(nei)
#                         stack.append(nei)
#             else:
#                 return False
#         return True

# Union Find - 级联 O(N*a(P)+p) 约等于 O(N+P)
from collections import defaultdict
def Zero():
    return 0
class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        m = len(words1)
        n = len(words2)
        if m != n:
            return False 
        
        def mix(word1, word2):
            p1 = find(word1)
            p2 = find(word2)
            if p1 != p2:
                uni[p1] = p2
            
        def find(word):
            if uni[word] != word:
                uni[word] = find(uni[word])
            return uni[word]
        
        uni = defaultdict(Zero)  # key 不存在时 返回0
        for word1, word2 in pairs:
            # 对于pairs中的每对元素，若为出现过，先各自成树，然后合并
            if uni[word1] == 0:
                uni[word1] = word1
            if uni[word2] == 0:
                uni[word2] = word2
                
            mix(word1, word2)  # 合并
            
        for i in range(m):
            if words1[i] == words2[i]:
                continue
            elif not find(words1[i]) == find(words2[i]):
                    return False
                
        return True


words1 = ["great","acting","skills"]
words2 = ["fine","drama","talent"]
pairs = [["great","fine"],["drama","acting"],["skills","talent"]]
res = Solution().areSentencesSimilarTwo(words1, words2, pairs)
print(res)


# # 测试并查集

# data = {1: 1, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}

# def find(key):
#     if data[key] != key:
#         data[key] = find(data[key])
#     return data[key]

# print(find(6))
# print(data)
