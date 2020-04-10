# print(3 >> 1)
# print(3 << 1)
#
# # 取不大于key的最大偶数
# print(3 >> 1 << 1)
# print(4 >> 1 << 1)
# print(5 >> 1 << 1)
# print(6 >> 1 << 1)
# print(7 >> 1 << 1)
#
#
# # 奇数返回1
# print('-'*30)
# print(3 & 1)
# print(4 & 1)
# print(5 & 1)
# print(6 & 1)

n = 10
while n:
    n >>= 1
    print(n)

