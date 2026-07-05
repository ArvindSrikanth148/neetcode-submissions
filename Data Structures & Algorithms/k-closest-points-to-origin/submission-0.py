class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h=[]
        for i in range(len(points)):
            dist=points[i][0]*points[i][0]+points[i][1]*points[i][1]
            heapq.heappush_max(h,[dist,points[i][0],points[i][1]])
            if len(h)>k:
                heapq.heappop_max(h)
        res=[]

        for i in range(len(h)):

            d,x,y=heapq.heappop_max(h)
            res.append([x,y])
        return res
        


        