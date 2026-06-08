class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index=0
        index2=0
        for i in range(len(numbers)):
            l=numbers.copy()
            x=l.pop(i)
            if target-numbers[i] in l :
                index=i
                break
        v= target-numbers[index]
        for i in range(len(numbers)):
            if v==numbers[i]:
                index2=i
                break
        return [index+1,index2+1]
        