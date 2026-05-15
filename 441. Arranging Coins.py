class Solution:
    def arrangeCoins(self, n):
        row = 0
        i = 1
        
        while n >= i:
            n -= i
            row += 1
            i += 1
            
        return row