class Solution:
    def romanToInt(self, s):
        def getValue(c):
            if c == 'I': return 1
            if c == 'V': return 5
            if c == 'X': return 10
            if c == 'L': return 50
            if c == 'C': return 100
            if c == 'D': return 500
            if c == 'M': return 1000
            return 0

        total = 0
        n = len(s)
        
        for i in range(n):
            current_val = getValue(s[i])
            
            if i + 1 < n and current_val < getValue(s[i + 1]):
                total -= current_val
            else:
                total += current_val
                
        return total
