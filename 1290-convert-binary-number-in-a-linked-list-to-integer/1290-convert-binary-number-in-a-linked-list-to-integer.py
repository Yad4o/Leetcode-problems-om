class Solution(object):
    def getDecimalValue(self, head):
        i = 0
        while head:
            i = i * 2 + head.val
            head = head.next
        return i