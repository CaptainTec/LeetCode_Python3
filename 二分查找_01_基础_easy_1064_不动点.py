"""
Given an array A of distinct integers sorted in ascending order, 
return the smallest index i that satisfies A[i] == i.  

Return -1 if no such i exists.

"""

class Solution:
    def fixedPoint(self, A):
        """
        type: A: List[int]
        rtype : int
        """
        if not A: return -1

        left, right = 0, len(A) - 1
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] < mid:
                left = mid + 1
            else:# 当存在多个 A[i] == i时，该判断条件会使mid逐渐减少
                right = mid  # 题意就是让找最小
        return left if A[left] == left else -1