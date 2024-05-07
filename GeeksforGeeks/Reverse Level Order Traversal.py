""" Given a binary tree of size n, find its reverse level order traversal. ie- the traversal must begin from the last 
level.

Example 1:

Input :
        1
      /   \
     3     2

Output: 
3 2 1
Explanation:
Traversing level 1 : 3 2
Traversing level 0 : 1

Example 2:

Input :
       10
      /  \
     20   30
    / \ 
   40  60

Output: 
40 60 20 30 10
Explanation:
Traversing level 2 : 40 60
Traversing level 1 : 20 30
Traversing level 0 : 10
Your Task: 
You don't need to read input or print anything. Complete the function reverseLevelOrder() which takes the root of the
tree as input parameter and returns a list containing the reverse level order traversal of the given tree.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 104  """

#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def reverseLevelOrder(root):
    # code here
    if not root:
        return []

    queue = [root]
    stack = []

    while queue:
        node = queue.pop(0)
        stack.append(node.data)

        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)

    result = []
    while stack:
        result.append(stack.pop())

    return result

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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ans = reverseLevelOrder(root)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends