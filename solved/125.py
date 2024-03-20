class Solution:
    def isPalindrome(self, s: str) -> bool:
        processedS = ""
        for character in s:
            if character.isalnum():
                processedS += character.lower()

        if len(processedS) == 0:
            return True

        if len(processedS)%2 == 0: ## if even length (abba)
            if (processedS[0:int(len(processedS)/2)] == processedS[int(len(processedS)/2)::][::-1]):
                return True
            
        else:
            if (processedS[0:int(len(processedS)//2)] == processedS[int(len(processedS)//2)+1::][::-1]):
                return True
            
        return False



# Test Case
runSolution = Solution()

print(runSolution.isPalindrome("Never a foot too far, even."))