class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res
    def backtrack(self ,subset,nums,pick:List[bool]):
        if len(subset)==len(nums):
            self.res.append(subset.copy())
            return
        for i in range(len(nums)):
            if not pick[i]:
                subset.append(nums[i])
                pick[i]=True
                self.backtrack(subset,nums,pick)
                subset.pop()
                pick[i]=False


            
        
        