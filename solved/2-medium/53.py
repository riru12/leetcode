from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])

        return max(nums)

# Test Case
runSolution = Solution()

print(runSolution.maxSumSubarray([1,2,-1]))