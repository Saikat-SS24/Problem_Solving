""" Given a Binary Tree of N edges. The task is to convert this to a Circular Doubly Linked List (CDLL) in-place. The 
left and right pointers in nodes are to be used as previous and next pointers respectively in CDLL. The order of nodes
in CDLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) 
must be head node of the CDLL.

Example 1:

Input:
      1
    /   \
   3     2
Output:
3 1 2 
2 1 3
Explanation: After converting tree to CDLL
when CDLL is is traversed from head to
tail and then tail to head, elements
are displayed as in the output.

Example 2:

Input:
     10
   /    \
  20    30
 /  \
40  60
Output:
40 20 60 10 30 
30 10 60 20 40
Explanation:After converting tree to CDLL,
when CDLL is is traversed from head to
tail and then tail to head, elements
are displayed as in the output.
Your Task:
You don't have to take input or print anything. Complete the function bTreeToCList() that takes root as a parameter and
returns the head of the list. The driver code prints the linked list twice, first time in the right order, and another 
time in reverse order.

Constraints:
1 <= N <= 103
1 <= Data of a node <= 104

Expected time complexity: O(N)

Expected auxiliary space: O(h) , where h = height of tree """


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
        


# } Driver Code Ends
#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

'''

class Solution:
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        #Your code here
        def walk(n):
            if not n:
                return None, None
            lf, le = walk(n.left)
            rf, re = walk(n.right)
            if le:
                n.left = le
                le.right = n
            if rf:
                n.right = rf
                rf.left = n
            if not lf:
                lf = n
            if not re:
                re = n
            return lf, re
        
        h, t = walk(root)
        h.left = t
        t.right = h
        return h


#{ 
 # Driver Code Starts.
def displayList(head):
    itr=head
    while(itr.right!=head):
        print(itr.data,end=" ")
        itr=itr.right
    print(itr.data,end=" ")
    print()
    head = itr
    while(itr.left!=head):
        print(itr.data,end=" ")
        itr=itr.left
    print(itr.data, end=" ")
    
 
    
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
        head=Solution().bTreeToClist(root)
        displayList(head)
        print()
        
        

        




# } Driver Code Ends