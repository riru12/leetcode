from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for n in range(1,amount+1):
            for c in coins:
                if n-c >= 0:
                    dp[n] = min(1 + dp[n-c], dp[n])
        return dp[amount]

runSolution = Solution()

print(runSolution.coinChange([1,2,3],5))