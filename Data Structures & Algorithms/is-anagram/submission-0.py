class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for char in s:
            if char in dict1:
                dict1[char] += 1  # Increment if exists
            else:
                dict1[char] = 1   # Initialize if not exists
        for char in t:
            if char in dict2:
                dict2[char] += 1  # Increment if exists
            else:
                dict2[char] = 1   # Initialize if not exists
        if dict1 == dict2:
            return True
        return False

