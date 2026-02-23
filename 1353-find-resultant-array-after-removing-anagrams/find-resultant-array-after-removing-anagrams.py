class Solution:
    def removeAnagrams(self, words):
        result = []
        
        for word in words:
            # If result is empty OR current word is NOT an anagram of last kept word
            if not result or sorted(word) != sorted(result[-1]):
                result.append(word)
        
        return result