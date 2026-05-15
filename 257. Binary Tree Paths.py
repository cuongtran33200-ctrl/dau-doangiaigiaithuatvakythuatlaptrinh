# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root):
        res = []
        
        def dfs(node, path):
            if not node:
                return
            
            # thêm node hiện tại vào path
            path += str(node.val)
            
            # nếu là lá → lưu kết quả
            if not node.left and not node.right:
                res.append(path)
                return
            
            # đi tiếp xuống dưới
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)
        
        dfs(root, "")
        return res