class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for(string s : strs){
            result+= to_string(s.size()) + "#" + s;
        }
        cout << result;

        return result;

    }

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while (i < s.length() ){
            int j = i;
            while ( s[j] != '#') {
                j++;
            }

            int length = stoi(s.substr(i, j - i));

            i = j + 1;

            j = length + i;

            result.push_back(s.substr(i, length));

            i = j;

        }
        return result;
        

    }
};
