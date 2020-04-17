"""
方法一：暴力匹配 --> O(n^2)

方法二：滑动窗口 --> O(n)
"""

# 方法一：暴力匹配 --> O(n^2)
# class Solution:
#     from collections import Counter
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         if not s or not words:
#             return []

#         # def load_dict(words):
#         #     data_dict = {}
#         #     for one in words:
#         #         if one in data_dict:
#         #             data_dict[one] += 1
#         #         else:
#         #             data_dict[one] = 1
#         #     return data_dict
        
#         def judge(j, s):
#             data_dict = Counter(words)
#             while s[j: j+word_len] in data_dict:
#                 data_dict[s[j: j+word_len]] -= 1
#                 if not data_dict[s[j: j+word_len]]:  # 为0
#                     del data_dict[s[j: j+word_len]]

#                 if not len(data_dict):  # 为空
#                     return True
#                 j += word_len
#             return False

#         res = []
#         word_len, words_len = len(words[0]), len(words)
#         i = 0
#         while i < len(s) - word_len*words_len + 1:
#             j = i
#             if judge(j, s):
#                 res.append(i)
#                 if len(set(words)) == 1 and len(set(list(s))) == 1:  # 特判 "aaaaaaaa" 和 ["aa","aa"]
#                     i += 1
#                 else:
#                     i += word_len
#             else:
#                 i += 1
#         return res


# 方法二：滑动窗口 --> O(n)
class Solution:
    def findSubstring(self, s, words):
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            # print(cur_Counter)
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                cur_Counter[w] += 1
                # print(cur_Counter)
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[left:left+one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num :
                    res.append(left)
            # break
        return res
