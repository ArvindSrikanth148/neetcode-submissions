class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        t=0 
        l=[]
        for i in range(len(nums)):
            if (target-nums[i]) in d.keys():
                t=i
                d[nums[i]]=target -nums[i]
                
                break
            d[nums[i]]=target -nums[i]

        
        for i in range(t):
            if i!=t and d[nums[t]]==nums[i]:
                l=[i,t]
        return l
    



                

          
        
        