"""
给出一个按 非递减 顺序排列的数组 nums，和一个目标数值 target。
假如数组 nums 中绝大多数元素的数值都等于 target，则返回 True，否则请返回 False。

所谓占绝大多数，是指在长度为 N 的数组中出现必须 超过 N/2 次。

思路：
先找中间值 num[mid], 然后在[left, mid]中找第一次出现num[mid]的值的下标first_index
再判断first_index + len(nums)//2 是否仍然等于target
"""

# Time：O(logN)
class Solution:
    # def isMajorityElement(self, nums: List[int], target: int) -> bool:
    def isMajorityElement(self, nums, target):
        left, right = 0, len(nums)
        right = left + (right-left) // 2
        mid_data = nums[right]
        if mid_data != target: return False

        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] == mid_data:
                right = mid
            else:
                left = mid + 1
        return True if left+len(nums)//2 < len(nums) and nums[left+len(nums)//2] == target else False


# 递归 Time：O(N)
class Solution2:
    def isMajorityElement2(self, nums, target):
        def fun(nums,left,right,target):
            if right < left:
                return 0
            mid  = (left+right)//2
            if nums[mid] == target:
                return fun(nums,left,mid-1,target) + fun(nums,mid+1,right,target) + 1
            else:
                return fun(nums,left,mid-1,target) + fun(nums,mid+1,right,target)
        n = len(nums)
        print(fun(nums,0,n-1,target))
        return True if fun(nums,0,n-1,target) > n/2 else False