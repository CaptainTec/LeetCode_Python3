# 字典
# class Solution:
#     def areSentencesSimilar(self, words1, words2, pairs):
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
#         for i in range(len_w1):
#             if words2[i] == words1[i] or words2[i] in data_dict[words1[i]]:
#                 continue
#             else:
#                 return False
#         return True


# 一种更简洁的写法，只用 set
class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        words1, words2: List[str]
        pairs: List[List[str]]
        return: bool
        """
        if len(words1) != len(words2):
            return False
        pairs = set(map(tuple, pairs))
        # return all(words1[i] == words2[i] or (words1[i], words2[i]) in pairs or (words2[i], words1[i]) in pairs for i in range(len(words1)))
        return all(w1 == w2 or (w1, w2) in pairs or (w2, w1) in pairs for w1, w2 in zip(words1, words2))



words1 = ["great","acting","skills"]
words2 = ["fine","drama","talent"]
pairs = [["great","fine"],["drama","acting"],["skills","talent"]]
res = Solution().areSentencesSimilar(words1, words2, pairs)
print(res)
