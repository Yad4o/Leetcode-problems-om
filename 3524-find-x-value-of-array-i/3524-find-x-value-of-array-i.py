class Solution:
    def resultArray(self, nums, k):
        # ans[x] will store the number of valid subarrays with product % k == x
        ans = [0] * k 
        
        # dp[r] stores the number of subarrays ending at the previous position 
        # whose product modulo k is equal to r
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            # 1. Start a brand new single-element subarray with the current 'num'
            new_dp[num_mod] += 1
            
            # 2. Extend all existing valid subarrays ending at the previous element
            for r in range(k):
                if dp[r] > 0:
                    new_remainder = (r * num_mod) % k
                    new_dp[new_remainder] += dp[r]
            
            # 3. Accumulate all valid subarrays ending at this position into the global answer
            for r in range(k):
                ans[r] += new_dp[r]
                
            # Roll over the DP array for the next iteration
            dp = new_dp
            
        return ans
