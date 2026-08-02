class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp={}
        dp[len(nums)-1]=1

        for i in range(len(nums)-2,-1,-1):
            cur=nums[i]
            dp[i]=1
            for j in range(i+1,len(nums)):
                if cur<nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    

        return max(dp.values())


        