# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root):
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        answer = 1
        
        while queue:
            level_size = len(queue)
            current_sum = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                current_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if current_sum > max_sum:
                max_sum = current_sum
                answer = level
            
            level += 1
        
        return answer