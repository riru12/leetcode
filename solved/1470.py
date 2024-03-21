from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        for i in range(n):
            out.append(nums[i])
            out.append(nums[i+n])
        return out
        

# Test Case
runSolution = Solution()

print(runSolution.shuffle([2,5,1,3,4,7], 3))