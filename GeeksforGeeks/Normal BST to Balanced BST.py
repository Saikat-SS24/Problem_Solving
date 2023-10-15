""" Given a Binary Search Tree, modify the given BST such that it is balanced and has minimum possible height. Return 
the balanced BST.

Example1:

Input:
       30
      /
     20
    /
   10
Output:
     20
   /   \
 10     30
Example2:

Input:
         4
        /
       3
      /
     2
    /
   1
Output:
      3            3           2
    /  \         /  \        /  \
   1    4   OR  2    4  OR  1    3   
    \          /                  \ 
     2        1                    4

Your Task:
The task is to complete the function buildBalancedTree() which takes root as the input argument and returns the root 
of tree after converting the given BST into a balanced BST with minimum possible height. The driver code will print the height of the updated tree in output itself.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Here N denotes total number of nodes in given BST.

Constraints:
1 <= N <= 105
1 <= Node data <= 109 """

#User function Template for python3

class Solution:
    def buildBalancedTree(self,root):
        #code here
        def inorder(root, l):
            if root is None:
                return 
            inorder(root.left, l)
            l.append(root.data)
            inorder(root.right, l)
        l = []
        inorder(root, l)

        def bst(arr, l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            a = Node(arr[mid])
            a.left = bst(arr, l, mid - 1)
            a.right = bst(arr, mid + 1, r)
            return a

        b = bst(l, 0, len(l) - 1)
        return b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
def height(root):
  if (root==None):
      return 0;
  else:
      lDepth = height(root.left);
      rDepth = height(root.right);
      if (lDepth > rDepth):
          return(lDepth+1);
      else:
          return(rDepth+1);
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        new=(ob.buildBalancedTree(root))
        print(height(new))
        
# } Driver Code Ends