""" You are given a binary tree and you need to remove all the half nodes (which have only one child). Return the root 
node of the modified tree after removing all the half-nodes.

Note: The output will be judged by the inorder traversal of the resultant tree, inside the driver code.

Examples:

Input: tree = 5
            /   \
          7     8
        / 
      2
Output: 2 5 8
Explanation: In the above tree, the node 7 has only single child. After removing the node the tree becomes  2<-5->8. 
Hence, the answer is 2 5 8 & it is in inorder traversal.
Input:  tree = 2   
              / \   
            7   5 
Output: 7 2 5
Explanation: Here there are no nodes which has only one child. So the tree remains same.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(height of the binary tree)

Constraints:
1<=number of nodes<=104 """


class Solution:
    def RemoveHalfNodes(self, node):
        #code here
        def remove(n):
            if not n or not n.left and not n.right:
                return n
            
            if n.left and n.right:
                n.left = remove(n.left)
                n.right = remove(n.right)
                return n
            elif n.left:
                return remove(n.left)
            else:
                return remove(n.right)
        
        return remove(node)


#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(s):
    if len(s) == 0 or s[0] == 'N':
        return None

    ip = s.split()
    root = Node(int(ip[0]))

    queue = []
    queue.append(root)

    i = 1
    while len(queue) > 0 and i < len(ip):
        currNode = queue.pop(0)
        currVal = ip[i]

        if currVal != 'N':
            currNode.left = Node(int(currVal))
            queue.append(currNode.left)

        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        if currVal != 'N':
            currNode.right = Node(int(currVal))
            queue.append(currNode.right)

        i += 1

    return root


def printInorder(root):
    if root is None:
        return

    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1

    while t > 0:
        s = data[index]
        root = buildTree(s)
        solution = Solution()
        fresh = solution.RemoveHalfNodes(root)
        printInorder(fresh)
        print()
        t -= 1
        index += 1

# } Driver Code Ends