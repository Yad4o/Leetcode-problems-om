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
            if first is None or x > first:
                first, second, third = x, first, second
            elif second is None or x > second:
                second, third = x, second
            elif third is None or x > third:
                third = x
        return third if third is not None else first 