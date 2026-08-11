class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l=r=0
        c=0
        while r< len(nums)-1: 
            f=0
            for i in range(l,r+1):
                f=max(f,i+nums[i])
            l=r+1
            r=f
            c =c+1
        return c


