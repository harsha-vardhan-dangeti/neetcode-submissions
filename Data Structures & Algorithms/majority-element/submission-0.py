class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        
        for i in range(len(nums)):
            hash_map[nums[i]]= hash_map.get(nums[i], 0) +1

        list_tuple = list(hash_map.items())
        list_tuple.sort(key=lambda x : x[1])
        return list_tuple[-1][0]
        