""" Given a Binary Search Tree of size N, find the Median of its Node values.

Example 1:

Input:
       6
     /   \
   3      8   
  /  \    /  \
 1    4  7    9
Output: 6
Explanation: Inorder of Given BST will be:
1, 3, 4, 6, 7, 8, 9. So, here median will 6.

Example 2:

Input:
       6
     /   \
   3      8   
 /   \    /   
 1    4   7   
Output: 5
Explanation:Inorder of Given BST will be:
1, 3, 4, 6, 7, 8. So, here median will
(4 + 6)/2 = 10/2 = 5. """

#User function Template for python3

def findMedian(root):
    # code here
    # return the median
    list=[]
    def inorder(r):
        if r: 
            inorder(r.left)
            list.append(r.data)
            inorder(r.right)
    inorder(root)
    length=len(list)
    mid=length//2
    if length%2==0:
        sum=list[mid-1]+list[mid]
        if sum%2==0:
            return sum//2
        else:
            return sum/2
    else:
        median=list[mid]
        return median
    return



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

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
    for _ in range(t):
        s=input()
        root=buildTree(s)
        print(findMedian(root))

# } Driver Code Ends