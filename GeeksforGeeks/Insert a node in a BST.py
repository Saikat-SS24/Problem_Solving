""" Given a BST and a key K. If K is not present in the BST, Insert a new Node with a value equal to K into the BST. 
If K is already present in the BST, don't modify the BST.

Example 1:

Input:
     2
   /   \   1     3
K = 4
Output: 
1 2 3 4
Explanation: 
After inserting the node 4
Inorder traversal will be 1 2 3 4.
Example 2:

Input:
        2
      /   \
     1     3
             \
              6
K = 4
Output: 
1 2 3 4 6
Explanation: 
After inserting the node 4
Inorder traversal of the above tree will be 1 2 3 4 6.
Your Task:
You don't need to read input or print anything. Your task is to complete the function insert() which takes the root of the BST and Key K as input parameters and returns the root of the modified BST after inserting K. 
Note: The generated output contains the inorder traversal of the modified tree.

Expected Time Complexity: O(Height of the BST).
Expected Auxiliary Space: O(Height of the BST).

Constraints:
1 <= Number of nodes initially in BST <= 105
1 <= K <= 109 """

#User function Template for python3

class Solution:
    #Function to insert a node in a BST. 
    def insert(self,root, Key):
        # code here
        def help(root, key):
            if key>root.data:
                if root.right:
                    help(root.right, key)
                else:
                    root.right = Node(key)
            elif root.data==key:
                return
            else:
                if root.left:
                    help(root.left, key)
                else:
                    root.left = Node(key)
        help(root, Key)

        return root
 


#{ 
 # Driver Code Starts

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

def inOrder(n):
    if n is None:
        return
    inOrder(n.left)
    print(n.data, end=' ')
    inOrder(n.right)

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        k=int(input())
        ob = Solution()
        ob.insert(root,k)
        inOrder(root)
        print()
# } Driver Code Ends