
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occurrences={}
        for i, ch in enumerate(s):
            if ch not in occurrences:
                occurrences[ch] = [i, i]
            else:
                occurrences[ch][1] = i
       
        st=0
        e=occurrences[s[0]][1]
        lengths=[]
        for i in range(len(s)):

            e=max(e,occurrences[s[i]][1])

            if i==e:
                lengths.append(e-st+1)
                st=i+1
                
        return lengths

            
            
        