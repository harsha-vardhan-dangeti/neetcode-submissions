class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for x in nums:
            hash_map[x] = hash_map.get(x, 0) + 1
        
        for value, count in hash_map.items():
            if count > 1:
                return True
        return False
    
        