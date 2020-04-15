"""
medium
"""
# 此题其实就是寻找[m,n]范围内二进制数高位（左边）没有变化的数，后面补上0即为所求的结果。

# 判断m、n是否相等，如果不相等，m+1会使m的二进制数末位进位，有进位说明m的末位肯定有0的情况，
# 0与任何数相与皆得0，所以结果的末位肯定是0。同理，不断右移1位进行比较，
# 直到最终 m=n 时，说明找到了[m,n]这个范围内高位没有变化的数，
# 左移相同位数得到的结果就是所求的值。


def rangeBitwiseAnd(m, n):  # [m, n]
    cnt = 0
    while m != n:
        # print(m, n)
        m >>= 1
        n >>= 1
        cnt += 1
    # print('->', m, n, cnt)
    n <<= cnt
    # print(n)
    return n


# rangeBitwiseAnd(6, 7)

# print(1 << 2 - 1)  # 先算后面的减法
print(1 << 2)
