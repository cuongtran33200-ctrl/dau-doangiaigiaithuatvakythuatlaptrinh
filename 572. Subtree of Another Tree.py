class Solution:
    def isSubtree(self, root, subRoot):
        
        # kiểm tra 2 cây có giống nhau không
        def isSame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            return isSame(a.left, b.left) and isSame(a.right, b.right)
        
        # duyệt cây chính
        def dfs(node):
            if not node:
                return False
            
            if isSame(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)