class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([v.lower() for v in list(s) if v.isalnum()])
        return s == s[::-1]