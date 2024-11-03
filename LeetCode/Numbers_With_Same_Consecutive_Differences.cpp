class Solution {
private:
    void dfs_backtrack(int n, int k, string& tmp, vector<int>& res){
        if( tmp.length() == n ){
            res.push_back(stoi(tmp));
            return;
        }
        char candidate1 = tmp.back() + k, candidate2 = tmp.back() - k;
        if( '0' <= candidate1 && candidate1 <= '9' ){
            tmp += candidate1;
            dfs_backtrack(n, k, tmp, res);
            tmp.pop_back();
        }
        if( candidate1 != candidate2 && '0' <= candidate2 && candidate2 <= '9' ){
            tmp += candidate2;
            dfs_backtrack(n, k, tmp, res);
            tmp.pop_back();
        }
    }
    
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int> res;
        // 1. for every numbers, we starts from 1-9
        // 2. Call a dfs_recursive call to complete the rest of them
        for(int startnum = 1; startnum < 10; startnum++){
            string tmp = "";
            tmp += ('0' + startnum);
            dfs_backtrack(n, k, tmp, res);
        } return res;
    }
};
