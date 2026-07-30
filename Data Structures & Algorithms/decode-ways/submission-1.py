class Solution:
    def numDecodings(self, s: str) -> int:
        l=[]
        for i in range(1,27): 
            l.append(str(i))
        memo={}
        def backtracking(i):
            ways=0
        
            if i in memo:
                return memo[i]
            if i >= len(s):
               return 1
            if s[i] =='0':
                return 0
            ways=backtracking(i+1)
            if i + 1 < len(s) and s[i:i+2] in l:
                ways+=backtracking(i+2)
            memo[i]=ways
            return ways
        
        return backtracking(0)
        
