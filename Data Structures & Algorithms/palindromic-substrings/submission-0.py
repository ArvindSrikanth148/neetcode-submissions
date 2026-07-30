class Solution:
    def countSubstrings(self, s: str) -> int:
        
        c=0

        for i in range(len(s)): 

            l,r=i,i

            while l>=0 and r<len(s) and s[l]==s[r]:
                c=c+1
                l=l-1
                r=r+1
         

            l,r=i,i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                c=c+1
                l=l-1
                r=r+1
        return c