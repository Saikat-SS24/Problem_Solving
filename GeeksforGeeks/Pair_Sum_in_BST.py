""" Given a Binary Search Tree(BST) and a target. Check whether there's a pair of Nodes in the BST with value summing 
up to the target. 

Examples:

Input: root = [7, 3, 8, 2, 4, N, 9], target = 12
Output: True
Explanation: In the binary tree above, there are two nodes (8 and 4) that add up to 12.

Input: root = [9, 5, 10, 2, 6, N, 12], target = 23
Output: False
Explanation: In the binary tree above, there are no such two nodes exists that add up to 23.

Constraints:
1 ≤ Number of Nodes ≤ 105
1 ≤ target ≤ 106 """

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
    

# } Driver Code Ends

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''

class Solution:
    def findTarget(self, root, target): 
        # your code here.
        s = set()
        def fun(root):
            if root == None:
                return False
            if target - root.data in s:
                return True
                
            s.add(root.data)
            
            return fun(root.left) or fun(root.right)
            
        
        return fun(root)

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        summ = int(input())
        root=buildTree(s)
        ans = Solution().findTarget(root,summ)
        if (ans==False):
            print(0)
        else:
            print(1)
        print("~")
# } Driver Code Ends