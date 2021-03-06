"""
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，
为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
示例 2:

输入: [[7,10],[2,4]]
输出: 1

解法：
堆 - heapq
"""
import heapq
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         if not intervals:  # 会议为空
#             return 0
#         intervals = sorted(intervals)
#         cnt = 1
#         meet_rooms = [intervals[0][1]]  # 存储最后一个会议的截止时间, 初始化先存储第一个会议的结束时间
#         for meeting in intervals[1:]:
#             key = False
#             for i in range(len(meet_rooms)):
#                 if meet_rooms[i] <= meeting[0]:  # 上一个会议的结束时间早于该会议的开始时间，可用此会议室
#                     meet_rooms[i] = meeting[1]
#                     key = True
#                     break
#             if not key:
#                 meet_rooms.append(meeting[1])  # 新增一个房间
#                 cnt += 1
#         return cnt


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])  # 将ntervals[0][1]压入堆中, 即第一个会议的结束时间

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:  # 如果在队列中（正使用会议室的会议）的最早结束时间早于下个即将开始的会议时间
                heapq.heappop(free_rooms)  # 从堆中弹出最小的元素

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)


