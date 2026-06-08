class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        u=len(s)-1
        
        s=s.lower()
        while l<=u:
            while l <= u and not ((ord(s[u])>=97 and ord(s[u])<= 122) or (ord(s[u])>=48 and ord(s[u])<=57 )):
        
                u=u-1
            while l <= u and not ((ord(s[l])>=97 and ord(s[l])<= 122) or (ord(s[l])>=48 and ord(s[l])<=57 )):
                l=l+1
            if s[u]!=s[l] and l<=u :                  
             return False

            u=u-1
            l=l+1

        return True


 


 
