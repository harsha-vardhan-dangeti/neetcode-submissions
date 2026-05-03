class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        map<int, int> hash_map;

        for(int i = 0; i < nums.size(); i++){
            hash_map[nums.at(i)]++;
        }

        for(auto &x : hash_map) {
            if (x.second > 1) {
                return true;
            } 
        }
        return false;
        

    }
};