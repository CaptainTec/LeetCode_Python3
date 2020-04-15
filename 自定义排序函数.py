"""
在 python2 中，如果想要自定义评价标准的话，可以这么做

def cmp(a, b):
  # 如果逻辑上认为 a < b ，返回 -1
  # 如果逻辑上认为 a > b , 返回 1
  # 如果逻辑上认为 a == b, 返回 0 
  pass

a = [2,3,1,2]
a = sorted(a, cmp)

但是在 python3 中，cmp 这个参数已经被移除了，那么在 python3 中应该怎么实现 python2 的 cmp 功能呢？

"""
import functools
# def cmpp(a, b):
#     if b < a:
#         return -1
#     if a < b:
#         return 1
#     return 0
# a = [1, 2, 5, 4]
# print(sorted(a, key=functools.cmp_to_key(cmpp)))

# 例子：给定一些含有两个元素的list，如[a1, a2], 对第一个元素按升序排序，若第一个元素相等，再对第二个元素降序排序
arr = [[3, 3], [3, 4], [3, 5], [2, 2], [2, 1], [2, 9], [4, 6], [1, 0], [1, 2]]

def cmp(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    elif a[1] < b[1]:
        return 1
    else:
        return -1
    return 0
print(sorted(arr, key=functools.cmp_to_key(cmp)))


"""
上面这个方法实现了降序排列，因为 -1 代表我们逻辑上认为 a<b ，而实际上 b<a 。

追溯 cmp_to_key 的源码，发现是这样的
def cmp_to_key(mycmp):
    # Convert a cmp= function into a key= function
    class K(object):
        __slots__ = ['obj']
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        __hash__ = None
    return K
"""

# Reference
# https://blog.csdn.net/u012436149/article/details/79952975?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2

arr = [1, 2, 3]
print(arr[:10])
