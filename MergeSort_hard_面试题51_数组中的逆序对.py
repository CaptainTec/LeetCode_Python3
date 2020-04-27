class Solution:
    # def reversePairs(self, nums: List[int]) -> int:
    def reversePairs(self, nums):

        def merge(left, mid, right, tmp):
            for i in range(left, right+1):
                tmp[i] = nums[i]
            i, j, index = left, mid+1, left
            while index <= right:
                if i > mid:
                    nums[index] = tmp[j]
                    j += 1
                elif j > right:
                    nums[index] = tmp[i]
                    i += 1
                elif tmp[i] < tmp[j]:
                    nums[index] = tmp[i]
                    i += 1
                else:
                    nums[index] = tmp[j]
                    self.cnt += mid - i + 1
                    print(right - j + 1)
                    j += 1
                index += 1

        def MergeSort(left, right, tmp):
            if left == right:  # 递归边界
                return
            mid = left + (right-left) // 2
            MergeSort(left, mid, tmp)
            MergeSort(mid+1, right, tmp)
            merge(left, mid, right, tmp)
        
        self.cnt = 0
        tmp = nums[:]
        MergeSort(0, len(nums)-1, tmp)
        return self.cnt


cnt = 0
arr = [5, 4, 3, 2, 1]
# tmp = [0] * len(arr)
# divide(0, len(arr)-1, tmp)
# print(arr)
# print(cnt)
res = Solution().reversePairs(arr)
print(arr)
print(res)
