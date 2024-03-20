class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
        
# Test Case
runSolution = Solution()

print(runSolution.lengthOfLastWord("test striiiiiiiing"))