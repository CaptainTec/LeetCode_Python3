class Solution:
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype List[int]
        """
        dists = [[] for _ in range(len(workers))]
        for i, (xw, yw) in enumerate(workers):
            for j, (xb, yb) in enumerate(bikes):
                dist = abs(xw - xb) + abs(yw - yb)
                dists[i].append((dist, i, j))
            dists[i].sort(reverse=True)
        
        for one in dists:
            print(one)
        heap = [d.pop() for d in dists]  # 二维数组dists中的一维数组的最后一个元素pop出来, 构建heap
        print(heap)
        import heapq
        heapq.heapify(heap)
        res = [-1] * len(workers)
        allocated = 0
        used_bikes = [False] * len(bikes)

        while allocated < len(workers):
            dist, i, j = heapq.heappop(heap)
            if not used_bikes[j]:
                res[i] = j  # 若worker被分配之后, 就不会再遍历到该worker
                allocated += 1
                used_bikes[j] = True
            else:  
                # 这里是因为heap中是按worker的人数来判断的, 
                # 当前的bike_j不符合要求，还要对worker_i分配下一辆车
                heapq.heappush(heap, dists[i].pop())
        
        return res

w = [[0,0],[2,1]]
b = [[1,2],[3,3]]
res = Solution().assignBikes(w, b)
print(res)