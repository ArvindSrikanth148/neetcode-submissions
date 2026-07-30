class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:len(nums)-1]))
    def helper(self, nums:List[int]): 
        # skip one or two 
        n=len(nums)
        if n==0: 
            return 0
        if n==1: 
            return nums[0]
        
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        if n==2:
            return dp[1]
        dp[2]=max(nums[0]+nums[2],nums[1])
        
        for i in range(3,n):
            dp[i]= nums[i]+max(dp[i-2],dp[i-3])
            
        return max(dp[n-1],dp[n-2])
        