class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1 
        r=0
        for i in piles:
            r=max(i,r)
        mid=0
        res=r
        while l<=r:

            mid=(l+r)//2
            hr=0 
            for i in piles:
                hr=hr+math.ceil(i/mid)
            
            if hr <=h:
                r=mid-1
                res=mid
                print(mid)
            else :
                l=mid+1
        return res
                
                
             
        
