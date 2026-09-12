class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        q = deque()  # Stores indices of elements
        
        for i, x in enumerate(nums):
            # Remove smaller elements from the back as they are useless
            while q and nums[q[-1]] <= x:
                q.pop()
                
            q.append(i)
            
            # Remove the front element if it is outside the current sliding window
            if q[0] <= i - k:
                q.popleft()
                
            # Add the maximum element of the current window to the result
            if i >= k - 1:
                ans.append(nums[q[0]])
                
        return ans