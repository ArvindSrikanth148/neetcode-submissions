class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        l=0 
        u=len(numbers)-1
        
        while l<u:

            if numbers[u]==target-numbers[l]:
                return [l+1,u+1]
            elif numbers[u]+numbers[l]>target:
                u=u-1
            elif numbers[u]+numbers[l]<target:
                l=l+1
