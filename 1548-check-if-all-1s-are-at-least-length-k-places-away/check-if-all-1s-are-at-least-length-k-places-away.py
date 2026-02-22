class Solution:
    def kLengthApart(self, nums, k):
        prev_index = -1
        
        for i in range(len(nums)):
            if nums[i] == 1:
                if prev_index != -1:
                    if i - prev_index - 1 < k:
                        return False
                prev_index = i
        
        return True