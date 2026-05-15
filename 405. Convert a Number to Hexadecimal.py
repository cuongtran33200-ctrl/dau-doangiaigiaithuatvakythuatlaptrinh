class Solution:
    def toHex(self, num):
        if num == 0:
            return "0"
        
        num &= 0xFFFFFFFF
        hex_chars = "0123456789abcdef"
        res = ""
        
        while num > 0:
            digit = num & 15
            res = hex_chars[digit] + res
            num >>= 4
        
        return res