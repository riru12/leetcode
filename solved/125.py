class Solution:
    def isPalindrome(self, s: str) -> bool:
        processedS = ""
        for character in s:
            if character.isalnum():
                processedS += character.lower()

        if len(processedS) == 0:
            return True

        if (processedS==processedS[::-1]):
            return True

        return False



# Test Case
runSolution = Solution()

print(runSolution.isPalindrome("Never a foot too far, even."))