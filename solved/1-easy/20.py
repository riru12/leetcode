class Solution:
    def isValid(self, s: str) -> bool:
        matches = {")":"(",
                   "]":"[",
                   "}":"{"}
        stack = []

        for i in range(len(s)):
            if s[i] in matches.values():            ## if an opening character
                stack.append(s[i])
            else:                                   ## if an ending character
                if stack:                           ## if non-empty
                    if stack[-1] == matches[s[i]]:
                        stack.pop()
                    else:
                        return False
                else:                               ## if empty
                    return False
                
        if stack: return False
        else: return True

# Test Case
runSolution = Solution()

print(runSolution.isValid("()"))