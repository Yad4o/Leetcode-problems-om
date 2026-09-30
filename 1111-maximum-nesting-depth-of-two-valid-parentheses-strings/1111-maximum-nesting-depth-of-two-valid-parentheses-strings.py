class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        ans = []
        depth = 0
        
        for x in seq:
            if x == '(':
                ans.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                ans.append(depth % 2)
        return ans
