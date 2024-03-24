from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ## 2D Dynamic Prog solution inspired from Kadane's algorithm
        for i in range(len(triangle)):
            if i != 0:
                for j in range(len(triangle[i])):
                    op1 = float('inf')
                    op2 = float('inf')

                    ## check upper left
                    if j != 0: ## if NOT on the left end of the pyramid
                        op1 = triangle[i][j]+triangle[i-1][j-1]

                    ## check upper right
                    if j != len(triangle[i-1]): ## if NOT on the right end of the pyramid
                        op2 = triangle[i][j]+triangle[i-1][j]

                    triangle[i][j] = min(op1,op2)

        return min(triangle[-1])
        

# Test Case
runSolution = Solution()

print(runSolution.minimumTotal([[-1],[2,3],[1,-1,-3]]))