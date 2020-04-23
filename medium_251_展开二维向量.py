class Vector2D:

    def __init__(self, v):
        """type: List[List[int]]"""
        import collections
        self.data = collections.deque()
        for one in v:
            self.data.extend(one)
        print(self.data)


    def next(self):
        """rtype: int"""
        # 双端队列 popleft 时间复杂度是O(1)
        # 列表 pop(0) 时间复杂度是O(n)
        return self.data.popleft()


    def hasNext(self):
        """rtype: bool"""
        return True if len(self.data) else False




# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()