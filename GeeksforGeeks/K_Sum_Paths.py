""" Given a binary tree and an integer K. Find the number of paths in the tree which have their sum equal to K.
A path may start from any node and end at any node in the downward direction.
Since the answer may be very large, compute it modulo 109+7.

Example 1:

Input:      
Tree = 
          1                               
        /   \                          
       2     3
K = 3
Output: 
2
Explanation:
Path 1 : 1 + 2 = 3
Path 2 : only leaf node 3

Example 2:

Input: 
Tree = 
           1
        /     \
      3        -1
    /   \     /   \
   2     1   4     5                        
        /   / \     \                    
       1   1   2     6    
K = 5                    
Output: 
8
Explanation:
The following paths sum to K.  
3 2 
3 1 1 
1 3 1 
4 1 
1 -1 4 1 
-1 4 2 
5 
1 -1 5 
Your Task:  
You don't need to read input or print anything. Complete the function sumK() which takes root node and integer K as 
input parameters and returns the number of paths that have sum K. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(Height of Tree)

Constraints:
1 ≤ N ≤ 2*104
-105 ≤ Node Value ≤ 105
-109 ≤ K ≤ 109 """


#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import defaultdict

class Solution:
    def sumK(self,root,k):
        # code here
        ans = 0
        def walk(n, cache, p=0):
            nonlocal ans, k
            if not n:
                return
            cur = p+n.data
            ans += cache[cur-k]
            cache[cur] += 1
            walk(n.left, cache, cur)
            walk(n.right, cache, cur)
            cache[cur] -= 1
        cache = defaultdict(int)
        cache[0] = 1
        walk(root, cache)
        return ans%(10**9+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)
from collections import deque
from collections import defaultdict
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
        d=int(input())
        ob = Solution()
        print(ob.sumK(root,d))
        
# } Driver Code Ends