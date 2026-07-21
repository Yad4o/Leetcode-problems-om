# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head is not None and head.val == val :
            head = head.next
        if head is None:
            return None
        prev = head
        temp = head.next
        while temp is not None:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head