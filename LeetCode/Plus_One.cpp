class Solution {
public:
    vector<int> plusOne(vector<int> &digits)
    {
        int i, size = digits.size(), carry = 1;

        for (i = size - 1; i >= 0 && carry != 0; i--){
            carry += digits[i];
            digits[i] = carry % 10;
            carry = carry / 10;
        }

        if( carry != 0 ){
            digits.emplace(digits.begin(), 1);
        }

        return digits;
    }
};
