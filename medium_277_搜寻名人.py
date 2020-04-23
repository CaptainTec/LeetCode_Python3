# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    # def findCelebrity(self, n: int) -> int:
    def findCelebrity(self, n):
        """
        Time: O(n)
        不用暴力的两层循环

        因为根据名人的定义，若存在名人，所有其他人都认识他，总有一个人会链接到他
        """
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):  # 若该假定的celebrity 认识别人i，则更新假定的celebrity为i
                celebrity = i
        # 由于最多只会存在一个名人，上面的循环执行完毕后，假定的celebrity 和[celebrity+1, n-1] 都不认识
        for i in range(celebrity):  # 判断 celebrity 和 [0, celebrity-1] 是否认识
            if knows(celebrity, i):
                return -1
        for i in range(n):
            if not knows(i, celebrity):  # 若有人不是认识这个假定的celebrity，则该假定的celebrity 不是真正的celebrity
                return -1
        return celebrity

