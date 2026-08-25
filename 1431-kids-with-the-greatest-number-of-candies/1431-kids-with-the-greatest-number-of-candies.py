class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        mcandy = max(candies)
        result = []
        for x in candies:
            if (x + extraCandies) >= mcandy:
                result.append(True)
            else :
                result.append(False)
        return result