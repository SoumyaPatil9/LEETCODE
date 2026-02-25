class Solution:
    def hasAllCodes(self, s, k):
        needed = 1 << k  # 2^k
        seen = set()
        
        num = 0
        mask = needed - 1  # to keep only k bits
        
        for i in range(len(s)):
            # shift left and add new bit
            num = ((num << 1) & mask) | int(s[i])
            
            # start recording once window size >= k
            if i >= k - 1:
                seen.add(num)
                if len(seen) == needed:
                    return True
        
        return False