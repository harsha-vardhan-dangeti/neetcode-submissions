class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int n = nums.size();

        unordered_map<int, int> hash_map;

        for(int i=0; i<n; i++){
            int curr_sum = target - nums[i];

            if(hash_map.find(curr_sum) != hash_map.end()){
                return {hash_map[curr_sum], i};
            }

            hash_map.insert({nums[i], i});
        }

        return {};
        
    }
};
