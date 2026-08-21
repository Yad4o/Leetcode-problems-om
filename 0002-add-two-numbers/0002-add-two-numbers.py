# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        rem = 0
        while l1 or l2 or rem:
            if l1:
                v1 = l1.val 
            else:
                v1 = 0
            if l2:
                v2 = l2.val 
            else:
                v2 = 0
            
            total = v1 + v2 + rem

            rem = total // 10

            curr.next = ListNode(total % 10)

            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2: 
                l2 = l2.next
        return dummy.next
