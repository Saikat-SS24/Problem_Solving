class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int rows = mat.size(), cols = mat[0].size(), amount_of_paths = rows + cols - 1;
        vector<pair<int,int>> paths(amount_of_paths, {0, 0});
        for(int idx = 0; idx < amount_of_paths; idx++){
            paths[idx].first = rows > 0 ? --rows : 0;
            paths[amount_of_paths - idx - 1].second = cols > 0 ? --cols : 0;
        }
        for(pair<int,int>& start_point : paths){
            vector<int> curpath;
            for(int i = start_point.first, j = start_point.second; 
                i < mat.size() && j < mat[0].size(); i++, j++){
                curpath.push_back(mat[i][j]);
            } std::sort(curpath.begin(), curpath.end());
            for(int cnt = 0, i = start_point.first, j = start_point.second; 
                i < mat.size() && j < mat[0].size(); cnt++, i++, j++){
                mat[i][j] = curpath[cnt];
            }
        }
        return mat;
    }
};
