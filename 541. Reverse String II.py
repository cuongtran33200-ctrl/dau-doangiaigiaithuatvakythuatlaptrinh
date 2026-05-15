class Solution:
    def reverseStr(self, s, k) :
        s = list(s)  # chuyển sang list để sửa
        
        for i in range(0, len(s), 2 * k):
            # đảo k phần tử đầu
            s[i:i+k] = reversed(s[i:i+k])
        
        return "".join(s)