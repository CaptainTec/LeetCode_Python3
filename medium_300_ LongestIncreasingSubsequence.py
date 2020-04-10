"""
medium: LIS
"""


def lengthOfLIS(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i, -1, -1):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)
    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
lengthOfLIS(nums)



