"""
核心思想是：把待搜索的目标元素放在最后判断，每一次循环排除掉不存在目标元素的区间，
目的依然是确定下一轮搜索的区间；

特征：while (left < right)，这里使用严格小于 < 表示的临界条件是：
当区间里的元素只有 2 个时，依然可以执行循环体。换句话说，
退出循环的时候一定有 left == right 成立，这一点在定位元素下标的时候极其有用；

在循环体中，先考虑 nums[mid] 在满足什么条件下不是目标元素，
进而考虑两个区间 [left, mid - 1] 以及 [mid + 1, right] 里元素的性质，
目的依然是确定下一轮搜索的区间；

在退出循环以后，根据情况看是否需要对下标为 left 或者 right 的元素进行单独判断，
这一步叫「后处理」。在有些问题中，排除掉所有不符合要求的元素以后，
剩下的那 1 个元素就一定是目标元素。如果根据问题的场景，目标元素一定在搜索区间里，
那么退出循环以后，可以直接返回 left（或者 right）。

"""
def check(a):
    pass

# def search(nums: List[int], left: int, right: int, target: int) -> int:
def search(nums, left, right, target):
    while left < right:
        # 选择中位数时下取整
        mid = left + (right - left) // 2
        if check(mid):
            # 下一轮搜索区间是 [mid + 1, right]
            left = mid + 1
        else:
            # 下一轮搜索区间是 [left, mid]
            right = mid
    # 退出循环的时候，程序只剩下一个元素没有看到。
    # 视情况，是否需要单独判断 left（或者 right）这个下标的元素是否符合题意


# 2
# def search(nums: List[int], left: int, right: int, target: int) -> int:
def search2(nums, left, right, target):
    while left < right:
        # 选择中位数时上取整
        mid = left + (right - left + 1) // 2
        if check(mid):
            # 下一轮搜索区间是 [left, mid - 1]
            right = mid - 1
        else:
            # 下一轮搜索区间是 [mid, right]
            left = mid
    # 退出循环的时候，程序只剩下一个元素没有看到。
    # 视情况，是否需要单独判断 left（或者 right）这个下标的元素是否符合题意
