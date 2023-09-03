""" Given two Binary Trees. Check whether they are Isomorphic or not.

Note: 
Two trees are called isomorphic if one can be obtained from another by a series of flips, i.e. by swapping left and right children of several nodes. Any number of nodes at any level can have their children swapped. Two empty trees are isomorphic.
For example, the following two trees are isomorphic with the following sub-trees flipped: 2 and 3, NULL and 6, 7 and 8.
ISomorphicTrees

Example 1:

Input:
 T1    1     T2:   1
     /   \        /  \
    2     3      3    2
   /            /
  4            4
Output: No

Example 2:

Input:
T1    1     T2:    1
    /  \         /   \
   2    3       3     2
  /                    \
  4                     4
Output: Yes
Your Task:
You don't need to read input or print anything. Your task is to complete the function isomorphic() that takes the root nodes of both the Binary Trees as its input and returns True if the two trees are isomorphic. Else, it returns False. (The driver code will print Yes if the returned values are true, otherwise false.)

Expected Time Complexity: O(min(M, N)) where M and N are the sizes of the two trees.
Expected Auxiliary Space: O(min(H1, H2)) where H1 and H2 are the heights of the two trees.

Constraints:
1<=Number of nodes<=105 """

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
#User function Template for python3
import collections

class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, root1, root2): 
        #code here.
        if not root1 and not root2: return True
        que1,que2=deque(),deque()
        que1.append(root1)
        que2.append(root2)
        map1,map2=collections.defaultdict(list),collections.defaultdict(list)
        while que1:
            for _ in range(len(que1)):
                cur=que1.popleft()
                if cur.left:
                    que1.append(cur.left)
                    map1[cur.data].append(cur.left.data)
                if cur.right:
                    que1.append(cur.right)
                    map1[cur.data].append(cur.right.data)
        while que2:
            for _ in range(len(que2)):
                cur=que2.popleft()
                if cur.left:
                    que2.append(cur.left)
                    map2[cur.data].append(cur.left.data)
                if cur.right:
                    que2.append(cur.right)
                    map2[cur.data].append(cur.right.data)
        for i,j in map1.items():
            if i not in map2.keys():
                return False
            else:
                for v in j:
                    if v not in map2[i]:
                        return False
        return True

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s1=input()
        s2=input()
        root1=buildTree(s1)
        root2=buildTree(s2)
        if Solution().isIsomorphic(root1,root2):
            print('Yes')
        else:
            print('No')
# } Driver Code Ends