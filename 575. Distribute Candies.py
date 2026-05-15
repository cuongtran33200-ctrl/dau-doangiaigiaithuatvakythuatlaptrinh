class Solution:
    def distributeCandies(self, candyType):
        
        n = len(candyType)

        
        kinds = len(set(candyType))

        
        return min(kinds, n // 2)