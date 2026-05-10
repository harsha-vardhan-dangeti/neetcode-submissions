class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join(c.lower() for c in s if c.isalnum())
        return new_str == new_str[::-1]
        