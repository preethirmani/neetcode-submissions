class Solution:
    def isAlphaNumeric(self, c):
        return (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('0') and ord(c) <= ord('9'))
        
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not self.isAlphaNumeric(s[l]) and l < r:
                l += 1
            while not self.isAlphaNumeric(s[r]) and r > l:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True



   
        