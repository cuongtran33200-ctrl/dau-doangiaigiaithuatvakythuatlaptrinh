class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        
        # tính chiều cao bên trái
        left = root
        leftHeight = 0
        while left:
            leftHeight += 1
            left = left.left
        
        # tính chiều cao bên phải
        right = root
        rightHeight = 0
        while right:
            rightHeight += 1
            right = right.right
        
        # nếu là cây đầy
        if leftHeight == rightHeight:
            return (1 << leftHeight) - 1
        
        # không phải → chia nhỏ
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)