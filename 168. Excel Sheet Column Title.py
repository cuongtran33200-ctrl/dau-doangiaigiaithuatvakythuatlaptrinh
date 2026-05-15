class Solution(object):
    def convertToTitle(self, columnNumber):
        result = ""
        c = columnNumber
        
        while c > 0:
            c -= 1
            r = c % 26
            result = chr(r + ord('A')) + result
            c //= 26
        
        return result