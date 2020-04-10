"""
medium

"""


def combinationSum3(k, n):
    res = []

    def helper(k, i, tmp, target):
        print(k, i, tmp, target)
        if not k and not target:
            res.append(tmp)
            return
        for j in range(i, 10):
            if j > target:
                break
            helper(k-1, j + 1, tmp + [j], target - j)

    helper(k, 1, [], n)
    return res


# res = combinationSum3(3, 9)
# print(res)


print(__doc__)  # 输出""" *** """ 的内容
