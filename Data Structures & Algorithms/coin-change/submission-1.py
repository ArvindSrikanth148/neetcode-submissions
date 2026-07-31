class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0

        for a in range(1,amount+1):

            for c in coins: 
                if a >= c:
                   dp[a]=min(dp[a],dp[a-c]+1)
        return dp[amount] if dp[amount] != float('inf') else -1





















        memo={}
        def backtracking(amt):
            if amt in memo:
                return memo[amt]
            
            if amt == 0:
                return 0
            
            mini = float('inf')
            
            for c in coins:
                if amt - c >= 0:
                    val = backtracking(amt - c)
                    if val != float('inf'):
                        mini = min(mini, 1 + val)
            
            memo[amt] = mini
            return mini

        ans = backtracking(amount)
        return ans if ans != float('inf') else -1
            

          
        