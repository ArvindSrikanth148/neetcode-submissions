class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        d={'[':']','{':'}','(':')'}

        for i in range(len(s)):
            if s[i] in d.keys():
                l.append(s[i])
            else:
                if len(l)==0:
                    return False
                else:
                 x=l.pop()
                if d[x]!=s[i]:
                    return False
        return len(l)==0
