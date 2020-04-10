# arr = [[1, 3], [20, 6], [8, 10], [15, 18]]
#
# # print(len([_ for _ in sorted(arr, key=lambda x: x[0])]))
# print([_ for _ in map(str, arr)])


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        print(sorted(map(str, nums)))
        # largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        # return '0' if largest_num[0] == '0' else largest_num


# print([1, 2, 3].pop())

# arr = ['a', 'b', 'c']
# tmp = ['a', 'c', '666', '666']
# arr += [_ for _ in tmp if _ not in arr]
# print(arr)

# 只要是后面(list, tuple) 中的一个就返回True
# print(isinstance([], (list, tuple)))  # True
# print(isinstance((), (list, tuple)))  # True
# print(isinstance({}, (list, tuple)))  # False


# third = [1, 2]
# a, _ = third
# print(a)


# a, = {'aaa': 666}  # 'aaa'
# a, = [2]           # 2
a, = (1, )           # 1
print(a)


