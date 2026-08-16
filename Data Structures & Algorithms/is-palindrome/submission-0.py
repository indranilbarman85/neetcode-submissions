class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join(char for char in s if char.isalnum())

        return False if clean_text.lower()!=clean_text[::-1].lower() else True

    
        