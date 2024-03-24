from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ## 2D Dynamic Prog solution inspired from Kadane's algorithm
        for i in range(1,len(triangle)): ## start with the second row
            for j in range(len(triangle[i])): ## for every item in each row
                op1 = float('inf')
                op2 = float('inf')

                ## check upper left
                if j != 0: ## if NOT on the left end of the pyramid
                    op1 = triangle[i][j]+triangle[i-1][j-1]

                ## check upper right
                if j != len(triangle[i-1]): ## if NOT on the right end of the pyramid
                    op2 = triangle[i][j]+triangle[i-1][j]


                ### e.g.
                ###             1
                ###         2       3
                ###     4       5 <--    6
                ###
                ###     in this case, 
                ###     triangle[i][j] = 5
                ###     op1 = 2
                ###     op2 = 3    
                

                triangle[i][j] = min(op1,op2) ## replace item with the lower option

        return min(triangle[-1])
        

# Test Case
runSolution = Solution()

print(runSolution.minimumTotal([[1],[2,3],[4,5,6]]))