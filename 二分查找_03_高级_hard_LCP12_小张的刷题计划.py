"""
题意概述
给定一个数组，将其划分成 MM 份，使得每份元素之和最大值最小，每份可以任意减去其中一个元素。

题解
如果不考虑每份可以任意减去一个元素，就是一个经典的二分问题，
具有单调最优的性质：如果最大值为 tt 可以满足条件划分，那么最大值为 t+1t+1 也可以。
所以就直接二分最大值 tt，找到最小满足条件的 tt 即可。

本题加了一个条件：每份可以删除任意一个数组。为了能够让最大值最小，显然每份中删去的一定是最大元素，
所以在二分判定可行性时，维护当前序列的最大值，然后记录删除最大值的结果，
也就是说二分的判定是：是否可以让每组删除最大值之后，总和都小于等于 tt。


"""

class Solution:
    # def minTime(self, time: List[int], m: int) -> int:
    def minTime(self, time, m):
        if m >= len(time): return 0

        left, right = 0, sum(time)
        while left < right:
            mid = left + (right - left) // 2
            cnt = 1  # 初始化为1，表示最后一组未超过mid
            total_mid = 0
            max_mid = 0
            for i in range(len(time)):
                total_mid += time[i]
                max_mid = max(max_mid, time[i])
                if total_mid - max_mid > mid:
                    cnt += 1
                    total_mid = time[i]
                    max_mid = time[i]
                
            if cnt > m:  # 分组太多, 大于天数, 需要增大mid 的值
                left = mid + 1
            else:
                right = mid
        return left

