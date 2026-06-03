class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        ans=[]
        strs.sort()
        for i in range(len(strs)):
            l = list(strs[i])
            l.sort()
            word = "".join(l)
            if word in d.keys():
                d[word].append(strs[i])
            else :
                d[word]=[strs[i]]
        for key,value in d.items():
            ans.append(value)
        ans.sort()
        return ans



            



       

                

