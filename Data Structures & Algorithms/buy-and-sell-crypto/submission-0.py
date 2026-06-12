class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min=prices[0]
        sum=0
        temp=0
        for i in range(len(prices)-1):
            temp=prices[i+1]-min
            if prices[i+1]<min:
                min=prices[i+1]
            if temp>sum:
                sum=temp
        return sum
            


