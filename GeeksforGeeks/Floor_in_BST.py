""" You are given a BST(Binary Search Tree) with n number of nodes and value x. your task is to find the greatest 
value node of the BST which is smaller than or equal to x.
Note: when x is smaller than the smallest node of BST then returns -1.

Example:

Input:
n = 7               2
                     \
                      81
                    /     \
                 42       87
                   \       \
                    66      90
                   /
                 45
x = 87
Output:
87
Explanation:
87 is present in tree so floor will be 87.
Example 2:

Input:
n = 4                     6
                           \
                            8
                          /   \
                        7       9
x = 11
Output:
9
Your Task:-
You don't need to read input or print anything. Complete the function floor() which takes the integer n and BST and 
integer x returns the floor value.

Constraint:
1 <= Noda data <= 109
1 <= n <= 105

Expected Time Complexity: O(n)
Expected Space Complexity: O(1) """


#User function Template for python3

class Solution:
    def floor(self, root, x):
        # Code here
        list = []
        def trav(root):
            if(root == None):
                return
            trav(root.left)
            list.append(x-root.data)
            trav(root.right)
        
        trav(root)
        ans=float("inf")
        for i in list:
            if(i >= 0):
                ans = min(ans,i)
        if(ans == float("inf")):
            return -1
        else:
            return(x-ans)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends