class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range (len(nums)):

            curr = target - nums[i]

            if curr in hash_map:
                return [hash_map[curr], i]
            else:
                hash_map[nums[i]] = i

            

        