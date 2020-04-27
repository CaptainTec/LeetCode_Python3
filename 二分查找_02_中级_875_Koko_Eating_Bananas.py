"""
binary search
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for one in piles:
                cnt += one // mid
                if one % mid:  # 若不能整除
                    cnt += 1
            if cnt > H:
                left = mid + 1
            else:
                right = mid  # cnt == H时，mid的值可能就是结果，但也可能需要缩小
        return left
