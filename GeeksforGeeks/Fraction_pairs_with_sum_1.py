""" Given a list of N fractions, represented as two lists numerator and denominator, the task is to determine 
the count of pairs of fractions whose sum equals 1.

Example 1:

Input:
N = 4
numerator = [1, 2, 2, 8]
denominator = [2, 4, 6, 12]
Output:
2
Explanation:
Fractions 1/2 and 2/4 sum to 1. Similarly fractions 2/6 and 8/12 sum to 1. So there are 2 pairs of fractions 
which sum to 1.

Example 2:

Input:
N = 5
numerator = [3, 1, 12, 81, 2]
denominator = [9, 10, 18, 90, 5]
Output:
2
Explanation:
Fractions 3/9 and 12/18 sum to 1. Similarly fractions 1/10 and 81/90 sum to 1. So there are 2 pairs of fractions 
which sum to 1. """

#User function Template for python3
from math import gcd

class Solution:
    def countFractions(self, n, numerator, denominator):
        # Your code here
        ans=0
        hash={}
        for num,den in zip(numerator,denominator):
            g=gcd(num,den)
            num//=g
            den//=g
            ans+=hash.get((den-num,den),0)
            hash[(num,den)]=hash.get((num,den),0)+1
        return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    numerator = list(map(int,input().split()))
    denominator = list(map(int,input().split()))
    ob = Solution()
    print(ob.countFractions(n,numerator,denominator))
# } Driver Code Ends