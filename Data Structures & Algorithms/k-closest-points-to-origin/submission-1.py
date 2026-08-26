class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        results = []
        mp = defaultdict(list)
        minHeap = []
        for pt in points:
            distance = self.dist(pt[0],0,pt[1],0)
            mp[distance].append(pt)
            print(distance)
            heapq.heappush(minHeap,(-distance,pt))
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        for p in minHeap:
            results.append(p[1])
        return results
            
    
    def dist(self,x1,x2,y1,y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)