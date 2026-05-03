#from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)

        for x in strs:

            count = [0]*26
            for i in range(len(x)):
                count[ord(x[i]) - ord('a')] += 1
            if tuple(count) not in hash_map:
                hash_map[tuple(count)] = []
            hash_map[tuple(count)].append(x)

        return list(hash_map.values())
