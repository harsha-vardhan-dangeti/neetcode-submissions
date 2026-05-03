class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}

        frequency = [[] for i in range(len(nums)+1)]

        for x in nums:
            hash_map[x] = hash_map.get(x, 0) + 1
        
        for num, count in hash_map.items():
            frequency[count].append(num)

        res = []

        for i in range(len(frequency)-1, 0, -1):
            for num in frequency[i]:
                res.append(num)

                if len(res) == k :
                    return res
     
            
