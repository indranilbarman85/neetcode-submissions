class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        for i in range(len(s)):
            new_text = s[:i] + s[i + 1 :]
            if new_text==new_text[::-1]:
                return True
        return False
                



        