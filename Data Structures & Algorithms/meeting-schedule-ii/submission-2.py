class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        ending_of_rooms = []

        for interval in intervals:
            if ending_of_rooms and ending_of_rooms[0] <= interval.start:
                heapq.heappop(ending_of_rooms)
            heapq.heappush(ending_of_rooms, interval.end)

        return len(ending_of_rooms)