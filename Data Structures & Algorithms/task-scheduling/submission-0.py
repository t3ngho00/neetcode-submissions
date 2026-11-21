class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxH = [count for count in counter.values()]
        heapq.heapify_max(maxH)

        q = deque() # pair of [count, at what time we can add the value back to maxH]
        time = 0
        while maxH or q:
            time+=1 
            if not maxH:
                time = q[0][1]
            else:
                count = heapq.heappop_max(maxH) - 1
                if count:
                    q.append([count, time+n])
            if q and q[0][1]== time: # if the first element of the queue is able to comeback to maxH, let it
                heapq.heappush_max(maxH, q.popleft()[0])
        return time