class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        l = 0 
        res = 0
        for r in range(len(s)):
            if s[r] in hash_map: 
                l = max(hash_map[s[r]]+1, l)
            hash_map[s[r]] = r
            res = max(res, r - l  + 1)
        return res