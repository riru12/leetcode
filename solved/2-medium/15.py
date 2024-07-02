from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue
            else:
                # Two Sum II
                remaining = 0 - nums[i]
                l,r = i+1, len(nums)-1

                while(l < r):
                    if (nums[l] + nums[r]) > remaining:
                        r = r - 1
                    elif (nums[l] + nums[r]) < remaining:
                        l = l + 1
                    else:
                        solutions.append([nums[i], nums[l], nums[r]])
                        l, r = l + 1, r - 1
                        while (l < r and nums[l]==nums[l-1]):
                            l = l + 1
                        while (l < r and nums[r]==nums[r+1]):
                            r = r - 1

        return solutions

runSolution = Solution()

print(runSolution.threeSum([-1,0,1,2,-1,-4]))