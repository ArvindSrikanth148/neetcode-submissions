class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        l=0
        r=0
        uni=[]
        max=1
        flag=True
        while r+1<len(s):
            
            
            if flag:
                uni.append(s[l])
                flag=False

            if s[r+1] not in uni:
                r=r+1
                uni.append(s[r])
            else:
                while s[r+1] in uni: 
                    uni.pop(0)
                    l=l+1
            win= r-l+1  
            if win> max:
                max=win
            
        return max

            


