class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} 

        for i in range(len(nums)):
            current_sum = target - nums[i]

            if current_sum in hash_map:
                return [hash_map[current_sum], i]
            else:
                hash_map[nums[i]] = i


            

        
        