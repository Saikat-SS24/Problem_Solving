class Solution {
public:
    double average(vector<int>& A) {
        return (accumulate(begin(A), end(A), 0.) - *max_element(begin(A), end(A)) - *min_element(begin(A), end(A))) / (A.size() - 2);
    }
};
