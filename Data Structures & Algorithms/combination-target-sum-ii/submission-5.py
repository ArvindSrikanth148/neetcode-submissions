class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(i, subset,sum):
            if sum==target:
                res.append(subset.copy())
                return
            if i==len(candidates) or sum>target:
                return 
            subset.append(candidates[i])
            backtrack(i+1,subset,sum+candidates[i])
            subset.pop()

            while i+1< len(candidates) and candidates[i]==candidates[i+1]:
                i=i+1

            backtrack(i+1,subset,sum)
        
        backtrack(0,[],0)
        return res