class Solution:
    def generateAbbreviations(self, word):
        if len(word) == 0:
            return [""]
        s = word[0]
        ans = []
        for w in self.generateAbbreviations(word[1:]):  # 递归
            j = 0
            while j < len(w) and w[j].isdigit():
                j += 1 
            if j == 0:
                ans.append(s+w) # 不缩写
                ans.append("1"+w) # 缩写
            else:
                ans.append(s+w) # 不缩写
                ans.append(str(int(w[:j])+1)+w[j:]) # 缩写
        return ans

"""
解题思路
使用回溯的算法，尝试替换前i个字符为数字，然后递归剩下的字符
定义回溯函数为backtrance(cur, i), cur表示i之前字符替换的结果，i表示已经处理到word的第i位
那么对于"word", 调用backtrance('', 0)

backtrance('', 0)

不替换， 递归调用backtrance('w', 1)
替换'w'为'1', 递归调用backtrace('1', 1)
替换'wo'为'2', 递归调用backtrace('2', 2)
...
对于backtrace('1', 1)

由于前面是'1', 所以不能替换为数字, 直接调用backtrace('1o', 2)

"""
# class Solution:
#     # def generateAbbreviations(self, word: str) -> List[str]:
#     def generateAbbreviations(self, word):
#         ans = []
#         def backtrace(cur='', i=0):
#             if i == len(word):
#                 ans.append(cur)
#                 return
            
#             backtrace(cur + word[i], i+1)
#             if not cur or not cur[-1].isdigit():  # cur 为空串 或者 cur[-1] 不为数字字符
#                 for j in range(i, len(word)):
#                     backtrace(cur+str(j-i+1), j+1)
#         backtrace()
#         return ans


# arr = 'word1'
# res = arr[-1].isdigit()
# print(res)

