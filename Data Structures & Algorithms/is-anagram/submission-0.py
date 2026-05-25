class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False 
        d1={}
        d2={}
        for i in range(len(s)):
            if s[i] in d1.keys():
             d1[s[i]]= 1+  d1[s[i]]
            else:
                d1[s[i]]=1
            if t[i] in d2.keys():
             d2[t[i]]= 1+  d2[t[i]]
            else:
                d2[t[i]]=1


        for key,value in d1.items():
            if key not in d2.keys():
                return False
            elif d2[key]!=value:
                return False 
        return True




