class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = "".join([ a for a in s if a.isalnum()]).lower()
        left = 0
        right = len(c) - 1
        while left < right:
            if c[left] == c[right]:
                left += 1
                right -= 1
            else:
                return False

        return True