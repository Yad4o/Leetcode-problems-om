class Solution:
    def productExceptSelf(self, nums):
        prod = 1
        zero = 0 
        for x in nums:
            if x != 0:
                prod *= x
            else:
                zero += 1
                
        ans = []
        if zero == 0:
            for x in nums:
                ans.append(prod/x)
        elif zero > 1:
            for x in nums:
                ans.append(x * 0)
        else:
            for x in nums:
                if x == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
        return ans