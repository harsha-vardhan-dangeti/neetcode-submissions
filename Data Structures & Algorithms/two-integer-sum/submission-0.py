class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for i in range(len(nums)):

            new_sum = target - nums[i]

            if new_sum in hash_map:
                return [hash_map[new_sum], i]
            
            hash_map[nums[i]] = i
        
        return 