class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals: return 0

        intervals = sorted(intervals)
        import heapq
        heap = []
        cnt = 1
        heapq.heappush(heap, intervals[0][1])
        for i in range(1, len(intervals)):
            top = heap[0]  # 如果只是想获取最小值而不是弹出，使用heap[0]
            if top <= intervals[i][0]:
                heapq.heappop(heap)
            else:
                cnt += 1
            heapq.heappush(heap, intervals[i][1])
        return cnt 
