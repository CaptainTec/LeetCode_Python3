# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    # def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
    def findInMountainArray(self, target, mountain_arr):
        """
        先 二分地查找 山顶的index

        然后左右两边查找target
        """
        left, right = 0, mountain_arr.length() - 1
        while left < right:  # 找山顶
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                left = mid + 1
            else:
                right = mid
        index = left
        # 山的左面
        left, right = 0, index
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        if mountain_arr.get(left) == target:
            return left
        
        # 山的右面
        left, right = index+1, mountain_arr.length() - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                right = mid
        return left if mountain_arr.get(left) == target else -1