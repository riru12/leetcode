from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)>2:
            for i in range(len(arr)):
                if i+2 < len(arr):
                    if arr[i]%2 != 0 and arr[i+1]%2 != 0 and arr[i+2]%2 != 0:
                        return True
        return False
                
runSolution = Solution()

print(runSolution.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))