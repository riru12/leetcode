class Solution:
    def climbStairs(self, n: int) -> int:
        counts = [1,1]
        for i in range(2,n+1):
            counts.append(counts[i-1]+counts[i-2])
        return counts[n]

runSolution = Solution()

print(runSolution.climbStairs(3))