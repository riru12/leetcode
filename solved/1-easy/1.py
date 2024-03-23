## Solution inspired from Nicholas T.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = dict()
        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in t.keys():
                return [t[comp],i]
            else:
                t[nums[i]] = i

# Test Case
runSolution = Solution()

print(runSolution.twoSum([3,2,4], 6))