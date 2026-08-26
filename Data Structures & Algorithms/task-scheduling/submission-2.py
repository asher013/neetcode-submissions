class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # what is important here: order of tasks and n, finding minimum number of cycles
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n]) # staged for next time we get to this task
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time


        