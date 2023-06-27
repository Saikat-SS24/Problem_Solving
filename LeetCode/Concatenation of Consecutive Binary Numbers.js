const concatenatedBinary = function(n) {
    let pow2 = 0;
    let result = 0;
    for(let i = 1; i < n + 1; i++) {
        if(!(i & (i - 1))) pow2++;
        result = (result * Math.pow(2, pow2) + i) % 1000000007;
    }
    return result;
};
