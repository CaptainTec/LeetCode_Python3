"""
# 二分查找的通常思路
如果做多了二分查找的题，这道题应该会有思路。
我们二分查找的时候，关键是要抓到施以查找的变量。即我们的left,right 和 mid 表示的是什么。

对于简单题，往往就是列表的一项。比如对一个排序好的列表找到一个相应的值的位置，
那么我们要施以查找的变量就是列表的下标，而缩小范围的依据就是列表的值。

对于复杂的题，往往这个施以查找的变量会比较难抓。它往往不是列表里的一个项，
而是一个要输出的值或判断依据做相应的变换。
难点就在于划分出哪些是施以查找的变量，哪些是这些变量的更新准则。
针对这题的二分查找思路


# 那么，对于这题，施以查找的变量是什么呢？
我们注意到题目里说的m个子数组各自和的最大值最小。
这是一个判断依据，也可以作为我们的施以查找的变量。
显然，如果对这个数组，每个数单独成一数组，那么子数组的各自和的最大值，就是所有数中的最大值。
而如果对这个数组不分组，那么子数组的各自和的最大值就是这个数组的和。
这两个值对应的就是 left 和 right，即全分组与不分组的结果。
套有我认为非常不错的这套「二分查找模板」，可以很容易写出这样的代码。

Reference:https://leetcode-cn.com/problems/split-array-largest-sum/solution/pao-ding-jie-niu-dai-ni-yi-bu-bu-shi-yong-er-fen-c/
"""

class Solution:
    # def splitArray(self, nums: List[int], m: int) -> int:
    def splitArray(self, nums, m):
        left, right = max(nums), sum(nums)
        while left < right:  # left == right 时 跳出循环
            mid = left + (right - left) // 2
            cnt = 1
            one_part = 0
            for one in nums:
                one_part += one
                if one_part > mid:
                    cnt += 1
                    one_part = one  # 最后会剩一个part，其值小于等于mid
            # if cnt == m:  # 两者相等时, mid的值是大于等于 需求的值的，所以这时可以并如到 cnt < m 的条件中
            #     pass
            if cnt > m:  # 分的个数大于m, 说明mid值太小了
                left = mid + 1
            else:
                right = mid
        return left