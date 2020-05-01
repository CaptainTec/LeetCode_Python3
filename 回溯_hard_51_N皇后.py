# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         res = []
#         from itertools import permutations
#         per = permutations([_ for _ in range(n)])
#         cnt = 0
#         key = True
#         for one in per:
#             key = True
#             for i in range(len(one)):
#                 for j in range(i+1, len(one)):
#                     if  i - j == one[i] - one[j] or j - i == one[i] - one[j]:
#                         key = False
#                         break
#             if key:
#                 matrix = []
#                 for i in range(len(one)):
#                     mid_list = ['.'] * n
#                     mid_list[one[i]] = 'Q'
#                     matrix.append(''.join(mid_list))

#                 res.append(matrix)
#         return res


class Solution:
    def solveNQueens(self, n):
        """
        n: int
        rtype: List[List[str]]
        """
        def could_place(row, col):  # 判断当前位置是否符合要求
            # cols[col] 、 hill_diagonals[row - col] 、 dale_diagonals[row + col] 三者全为0 返回True
            # cols[col]                   排除不同列
            #  hill_diagonals[row - col]  排除斜线
            # dale_diagonals[row + col]   排除反斜线
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
        # 当前位置 用 Queen 标记
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1
        
        # 取消当前位置 的 Queen 标记
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0
        
        # 将符合条件的结果 添加到output中
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        
        def backtrack(row = 0):  # 递归的过程 排除不同行
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)  # 回溯
        
        cols = [0] * n                      # 排除不同列
        hill_diagonals = [0] * (2 * n - 1)  # 排除斜线
        dale_diagonals = [0] * (2 * n - 1)  # 排除反斜线
        queens = set()
        output = []
        backtrack()
        return output
