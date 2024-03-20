from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m
        for num in nums2:
            nums1[i]=num
            i = i+1

        nums1.sort()

# Test Case
runSolution = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
runSolution.merge(nums1,m,nums2,n)

print(nums1)