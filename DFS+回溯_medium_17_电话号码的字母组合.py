class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:
    def letterCombinations(self, digits):

        def dfs(ss, n):
            if n == len(digits):
                res.append(ss)
                return 

            for character in data_dict[digits[n]]:
                ss += character
                dfs(ss, n+1)
                ss = ss[:-1]
                # 或将上面3行用下面1行替换
                # dfs(ss + character, n+1)

        data_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        dfs("", 0)
        return res

ss = '23'
res = Solution().letterCombinations(ss)
print(res)

