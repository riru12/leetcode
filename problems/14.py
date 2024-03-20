from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index=0
        done=0
        control = strs[0]

        while done!=1:
            for i in range(1,len(strs)):
                if strs[0][index] == strs[i][index]:
                    continue
                else:
                    done=1
                    break
            index = index+1
        
        return control[0:index-1]

# Test Case
runSolution = Solution()

print(runSolution.longestCommonPrefix(["flower","flow","flight"]))