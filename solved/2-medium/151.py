class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

# Test Case
runSolution = Solution()

print(runSolution.reverseWords("  hello world  "))