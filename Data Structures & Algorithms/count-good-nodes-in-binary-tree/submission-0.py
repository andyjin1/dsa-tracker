# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0 

        def dfs(root, path_max):
            nonlocal count
            if not root:
                return 
            
            if root.val >= path_max:
                path_max = root.val
                count += 1 
            
            dfs(root.left, path_max)
            dfs(root.right, path_max)

        dfs(root, float('-inf'))
        return count