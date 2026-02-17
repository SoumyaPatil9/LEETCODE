class Solution:
    def hasSameDigits(self, s):
        while len(s) > 2:
            new_s = []
            for i in range(len(s) - 1):
                digit_sum = (int(s[i]) + int(s[i + 1])) % 10
                new_s.append(str(digit_sum))
            s = "".join(new_s)
        
        return s[0] == s[1]
