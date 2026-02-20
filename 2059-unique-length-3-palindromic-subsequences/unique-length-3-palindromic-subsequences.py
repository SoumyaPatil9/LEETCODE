class Solution:
    def countPalindromicSubsequence(self, s):
        result = 0
        
        # Loop only through characters that appear in string
        for ch in set(s):
            first = s.find(ch)
            last = s.rfind(ch)
            
            if last - first > 1:
                middle_chars = set(s[first + 1:last])
                result += len(middle_chars)
        
        return result
