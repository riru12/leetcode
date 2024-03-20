from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_strLen = len(min(strs,key=len))
        if len(strs)<0 or shortest_strLen==0:
            return ""

        for i in range(0,shortest_strLen):
            letter = strs[0][i]
            if all(word[i]==letter for word in strs):
                continue
            else: 
                break
        
        return strs[0][:i]


# Test Case
runSolution = Solution()

print(runSolution.longestCommonPrefix(["flight","flower"]))

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_strLen = len(min(strs,key=len))
        if len(strs)<0 or shortest_strLen==0:
            return ""

        for i in range(0,shortest_strLen):
            letter = strs[0][i]
            if all(word[i]==letter for word in strs):
                continue
            else: 
                break
        
        return strs[0][0:i]
'''