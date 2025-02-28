""" Given a Binary Tree, your task is to return its In-Order Traversal.

An inorder traversal first visits the left child (including its entire subtree), then visits the node, and finally 
visits the right child (including its entire subtree).

Examples:

Input: root[] = [1, 2, 3, 4, 5] 
Output: [4, 2, 5, 1, 3]
Explanation: The in-order traversal of the given binary tree is [4, 2, 5, 1, 3].

Input: root[] = [8, 1, 5, N, 7, 10, 6, N, 10, 6]
Output: [1, 7, 10, 8, 6, 10, 5, 6]
Explanation: The in-order traversal of the given binary tree is [1, 7, 10, 8, 6, 10, 5, 6].

Constraints:
1 <= number of nodes <= 105
0 <= node->data <= 105  """


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        # code here
        res = []
        if root:
            res += self.inOrder(root.left)
            res.append(root.data)
            res += self.inOrder(root.right)
            
        return res

#{ 
 # Driver Code Starts
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
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        res = Solution().inOrder(root)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

        print("~")

# } Driver Code Ends