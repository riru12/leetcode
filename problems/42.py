from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(1,max(height)+1): ## trying each possible height (THIS IS SLOW)

            index = None
            for j in range(len(height)): ## going through the heights
                if index == None and height[j] >= i: ## finding the first instance
                    index = j
                elif index != None and height[j] >= i: ## finding the next instance
                    total = total + (j-index-1)
                    index = j
                
        return total
    
# Test Case
runSolution = Solution()

print(runSolution.trap([4,2,0,3,2,5]))

                