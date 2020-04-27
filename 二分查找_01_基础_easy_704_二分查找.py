"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = left + 1
            else:
                right = mid
        return left if nums[left] == target else -1