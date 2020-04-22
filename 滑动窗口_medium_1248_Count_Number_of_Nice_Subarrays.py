class Solution:
    def numberOfSubarrays(self, nums, k):
        """
        nums: List[int]
        k: int
        return: int
        思路： 统计每组符合要求的奇数下标左右偶数的数量，
        (left_num+1)*(right_num+1), 加1 是因为可以没有元素，然后求和即可
        """
        index_next = {}  #  # 奇数下标: 下一个奇数下标
        index_before = {}  #  # 前一个奇数下标: 奇数下标
        odd_index = []
        for i, one in enumerate(nums):
            if one%2:
                odd_index.append(i)
        if len(odd_index) < k:
            return 0

        for i, one in enumerate(odd_index):
            if i+1 < len(odd_index):
                index_next[one] = odd_index[i+1]
            if i-1 >= 0:
                index_before[one] = odd_index[i-1]
        
        cnt = 0
        i, j = 0, k-1
        while i <= len(odd_index) - k:
            left, right = 1, 1
            if odd_index[i] not in index_before:  # 左边
                left = odd_index[i] + 1
            else:
                left = odd_index[i] - index_before[odd_index[i]]
            if odd_index[j] not in index_next:  # 右边
                right = len(nums) - odd_index[j]
            else:
                right = index_next[odd_index[j]] - odd_index[j]
            cnt += left*right

            i += 1
            j += 1
        return cnt

nums = [1,1,2,1,1]
k = 3

res = Solution().numberOfSubarrays(nums, k)
print(res)