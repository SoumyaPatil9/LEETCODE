class Solution:
    def sumRootToLeaf(self, root):
        def dfs(node, current):
            if not node:
                return 0
            
            # Update binary value
            current = current * 2 + node.val
            
            # If leaf node, return current value
            if not node.left and not node.right:
                return current
            
            # Recur for left and right
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)