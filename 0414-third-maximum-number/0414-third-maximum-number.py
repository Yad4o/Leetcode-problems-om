class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = None
        for x in nums:
            if x in (first, second, third):
                continue
            
            if x > first:
                first, second, third = x, first, second
            elif x > second:
                second, third = x, second
            elif x > third:
                third = x
            
        return third if third is not None else first