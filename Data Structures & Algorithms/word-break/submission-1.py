class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={}

        def back(idx):
            if idx>=len(s): 
                return True
            if idx in memo :
                return memo[idx]

            p=False
            for w in wordDict: 
                if s[idx:idx+len(w)] == w:
                    p = back(idx+len(w))
                    if p==True:
                        break
            memo[idx]=p
            return p
        return back(0)        