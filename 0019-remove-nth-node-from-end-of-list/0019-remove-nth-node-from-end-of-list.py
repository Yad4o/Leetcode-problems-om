class Solution(object):
    def removeNthFromEnd(self, head, n):
        om = ListNode(0)
        om.next = head
        
        slow = fast = om
        
        for _ in range(n + 1):
            fast = fast.next
            
        while fast:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return om.next