""" Given an array arr of size N, determine whether this array represents an inorder traversal of a BST. 

Note: All keys in BST must be unique.

Example 1:

Input:
N = 3
arr = {2, 4, 5}
Output: 1
Explaination: 
Given array is inorder traversal for the following tree:
    4
   / \
  2   5

Example 2:

Input:
N = 3
arr = {2, 4, 1}
Output: 0
Explaination: 
Given array can not represent any BST.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isRepresentingBST() which takes 
the array arr[] and its size N as input parameters and returns 1 if array represents Inorder traversal of a BST, else 
returns 0.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ arr[i] ≤ 105 """


#User function Template for python3

class Solution:
    def isRepresentingBST(self, arr, N):
        # code here
        return 1 if sorted(arr)==arr else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.isRepresentingBST(arr, N))
# } Driver Code Ends