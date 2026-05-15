class Solution:
    def findTilt(self, root):
        self.total_tilt = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # tính độ nghiêng
            self.total_tilt += abs(left - right)
            
            # trả về tổng của subtree
            return left + right + node.val
        
        dfs(root)
        return self.total_tilt