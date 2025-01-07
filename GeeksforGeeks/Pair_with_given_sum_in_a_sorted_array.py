""" You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to 
target. It is given that the elements of the arr[] are in sorted order.

Note: pairs should have elements of distinct indexes. 

Examples :

Input: arr[] = [-1, 1, 5, 5, 7], target = 6
Output: 3
Explanation: There are 2 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.

Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: There are 6 pairs which sum up to 2 : {1, 1}, {1, 1}, {1, 1}, {1, 1}, {1, 1} and {1, 1}.

Input: arr[] = [-1, 10, 10, 12, 15], target = 125
Output: 0
Explanation: There is no such pair which sums up to 4.

Constraints:
-105 <= target <=105
2 <= arr.size() <= 105
-105 <= arr[i] <= 105  """

#User function Template for python3
from collections import defaultdict

class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        m = defaultdict(int)
        for e in arr:
            m[e] += 1
        
        ans = 0
        for e in arr:
            if e == target - e:
                ans += m[e] - 1
            else:
                ans += m[target-e]
            m[e] -= 1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends