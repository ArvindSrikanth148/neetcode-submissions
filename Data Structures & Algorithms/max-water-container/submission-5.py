class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l=0
        r=len(heights)-1
        maxi=0
        gmax=0
        while l<r:

            vol=min(heights[l],heights[r])*(r-l)
            
            if vol>maxi:
                #print(l,r,heights[l],heights[r])
                maxi=vol
            if max(heights[l],heights[r])>=gmax:
                 gmax=max(heights[l],heights[r])
                 if heights[l]>heights[r]:
                      r=r-1
                 else :
                      l=l+1
            else:
                if min(heights[l+1],heights[r])<min(heights[r-1],heights[l]):
                    
                    r=r-1
                else:
                    l=l+1
            
        return maxi

    



 

