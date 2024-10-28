""" Given an array arr consisting of positive integer numbers, remove all duplicate numbers.

Example:

Input: arr[] = [2, 2, 3, 3, 7, 5] 
Output: [2, 3, 7, 5]
Explanation: After removing the duplicates 2 and 3 we get 2 3 7 5.

Input: arr[] = [2, 2, 5, 5, 7, 7] 
Output: [2, 5, 7]

Input: arr[] = [8, 7] 
Output: [8, 7]

Constraints:
1<= arr.size() <=106
2<= arr[i] <=100 """

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def removeDuplicates(self, arr):
        # code here 
        res = []
        a = set()
        for i in arr:
            if i not in a:
                a.add(i)
                res.append(i)
                
        return res

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends