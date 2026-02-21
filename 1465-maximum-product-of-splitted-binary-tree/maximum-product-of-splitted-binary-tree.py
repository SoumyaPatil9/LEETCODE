# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        
        # Step 1: compute total sum
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)
        
        total = total_sum(root)
        self.max_product = 0
        
        # Step 2: compute subtree sums and update max product
        def subtree_sum(node):
            if not node:
                return 0
            
            left = subtree_sum(node.left)
            right = subtree_sum(node.right)
            
            current = node.val + left + right
            
            # product if we cut here
            product = current * (total - current)
            self.max_product = max(self.max_product, product)
            
            return current
        
        subtree_sum(root)
        
        return self.max_product % MOD