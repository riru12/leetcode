# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return
        

'''
from typing import List

class Solution:
    def mergeTwoLists(self, list1: List[int], list2: List[int]) -> List[int]:
        i,j = 0,0
        out = []
        while(i!=len(list1) and j!=len(list2)):
            if list1[i] < list2[j]: # smaller number in list1
                out.append(list1[i])
                i += 1
            elif list1[i] > list2[j]: # smaller number in list2
                out.append(list2[j])
                j += 1
            else: # equal
                out.append(list1[i])
                i += 1
        out = out + list1[i:] + list2[j:]
        return out

# Test Case
runSolution = Solution()

print(runSolution.mergeTwoLists([1,2],[1,2,3,4,5]))
'''