class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}

        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1
            hash_map[t[i]] = hash_map.get(t[i], 0) - 1

        # If all values are zero, the strings are anagrams
        return all(value == 0 for value in hash_map.values())
