""" Given an unsorted array arr and a number k which is smaller than size of the array. Find if the array contains 
duplicates within k distance.

Examples:

Input: arr[] = [1, 2, 3, 4, 1, 2, 3, 4] and k = 3
Output: false
Explanation: All duplicates are more than k distance away.

Input: arr[] = [1, 2, 3, 1, 4, 5] and k = 3
Output: true
Explanation: 1 is repeated at distance 3.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ k < arr.size()
1 ≤ arr[i] ≤ 105  """

#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        d = {}
        for i in range(len(arr) - k):
            for j in range(i, i + k + 1):
                d[arr[j]] = d.get(arr[j], 0) + 1
            if max(d.values()) > 1:
                return True
            d = {}
        return False
            
#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends