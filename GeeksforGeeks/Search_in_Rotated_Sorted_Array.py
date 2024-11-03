""" Given a sorted (in ascending order) and rotated array arr of distinct elements which may be rotated at some point 
and given an element key, the task is to find the index of the given element key in the array arr. The whole array arr 
is given as the range to search.

Rotation shifts elements of the array by a certain number of positions, with elements that fall off one end 
reappearing at the other end.

Note:- 0-based indexing is followed & returns -1 if the key is not present.

Examples :

Input: arr[] = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 10
Output: 5
Explanation: 10 is found at index 5.
Input: arr[] = [3, 5, 1, 2], key = 6
Output: -1
Explanation: There is no element that has value 6.
Expected Time Complexity: O(log n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 106
1 ≤ key ≤ 105  """

#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        for i in range(len(arr)):
            if arr[i] == key:
                return i
        
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))

# } Driver Code Ends