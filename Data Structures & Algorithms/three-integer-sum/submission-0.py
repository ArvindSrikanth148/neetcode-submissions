class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        nums.sort()
        for i in range(len(nums)):

            target = -nums[i]
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r]==target:
                    if [nums[i],nums[l],nums[r]] not in ans:
                       ans.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    r=r-1

                elif nums[l]+nums[r]<target:
                    l=l+1
                else:
                    r=r-1
        return(ans)


