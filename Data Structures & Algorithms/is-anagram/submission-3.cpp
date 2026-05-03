class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.length() != t.length()){
            return false;
        }
        
        vector<int> count(26);
        fill(count.begin(), count.end(), 0);

        for(int i=0; i<s.length() ; i++){
            count[int(s[i]) - int('a')]+=1;
            count[int(t[i]) - int('a')]-=1;
        }

        return all_of(count.begin(), count.end(), [](int x){return x == 0;});
    }
};
