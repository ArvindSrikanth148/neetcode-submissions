class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.limit=k
        self.h=nums 
        

        heapq.heapify(self.h)
        while len(self.h)>k:
            heapq.heappop(self.h)
    
    def add(self, val: int) -> int:

        heapq.heappush(self.h,val)
        if len(self.h)>self.limit:
            heapq.heappop(self.h)
        return self.h[0]

    
        
