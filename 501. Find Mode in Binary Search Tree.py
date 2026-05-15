class Solution:
    def findMode(self, root):
        from collections import defaultdict
        
        count = defaultdict(int)

        # duyệt cây
        def dfs(node):
            if not node:
                return
            count[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # tìm max frequency
        max_freq = max(count.values())

        # lấy các số có frequency = max
        return [k for k, v in count.items() if v == max_freq]