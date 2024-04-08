class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
    
# Test Case
runSolution = Solution()

print(runSolution.isPalindrome(121))