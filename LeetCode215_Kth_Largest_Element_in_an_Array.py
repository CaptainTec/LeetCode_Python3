"""
medium
"""


def findKthLargest(nums, k):
    def function(left, right, k):
        i, j = left, right
        mid = nums[i]
        while i < j:  # 一次快排
            while nums[j] < mid and i < j: j -= 1
            if nums[j] >= mid: nums[i] = nums[j]
            while nums[i] >= mid and i < j: i += 1
            if nums[i] < mid: nums[j] = nums[i]
        nums[i] = mid
        print(i, k-1, nums)
        # return nums
        if i == k-1: return nums[i]
        elif i < k-1:
            print(i+1, right, k-i-1)
            return function(i+1, right, k)
        else:
            return function(left, i-1, k)
    return function(0, len(nums)-1, k)

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # return list(sorted(nums, reverse=True))[k-1]  # 排序，一行解决
#         i, j = 0, len(nums)-1
#         mid = nums[i]
#         while i < j:  # 一次快排
#             while nums[j] < mid and i < j: j -= 1
#             nums[i] = nums[j]
#             while nums[i] >= mid and i < j: i += 1
#             nums[j] = nums[i]
#         nums[i] = mid
#         # return nums
#         if i == k-1: return nums[i]
#         elif i < k-1:
#             return self.findKthLargest(nums[i+1:], k-i-1)
#         else:
#             return self.findKthLargest(nums[:i], k)


# from numpy import random
#
#
# def findKthLargest(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#
#     def partition(left, right, pivot_index):
#         pivot = nums[pivot_index]
#         # 1. move pivot to end
#         nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
#
#         # 2. move all smaller elements to the left
#         store_index = left
#         for i in range(left, right):
#             if nums[i] < pivot:
#                 nums[store_index], nums[i] = nums[i], nums[store_index]
#                 store_index += 1
#
#         # 3. move pivot to its final place
#         nums[right], nums[store_index] = nums[store_index], nums[right]
#
#         return store_index
#
#     def select(left, right, k_smallest):
#         """
#         Returns the k-th smallest element of list within left..right
#         """
#         if left == right:  # If the list contains only one element,
#             return nums[left]  # return that element
#
#         # select a random pivot_index between
#         pivot_index = random.randint(left, right)
#
#         # find the pivot position in a sorted list
#         pivot_index = partition(left, right, pivot_index)
#
#         # the pivot is in its final sorted position
#         if k_smallest == pivot_index:
#             return nums[k_smallest]
#         # go left
#         elif k_smallest < pivot_index:
#             return select(left, pivot_index - 1, k_smallest)
#         # go right
#         else:
#             return select(pivot_index + 1, right, k_smallest)
#
#     # kth largest is (n - k)th smallest
#     return select(0, len(nums) - 1, len(nums) - k)


nums = [3, 2, 1, 5, 6, 4]
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 2
k = 4
print(findKthLargest(nums, k))
