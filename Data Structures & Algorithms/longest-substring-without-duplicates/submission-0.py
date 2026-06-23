class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        left = 0
        max_val = 0

        for right in range(len(s)):
            while s[right] in sub:
                sub.remove(s[left])
                left +=1
            sub.add(s[right])
            max_val = max(max_val, right - left + 1)
        return max_val