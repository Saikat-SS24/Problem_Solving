""" Given an integer X and an undirected acyclic graph with V nodes, labeled from 0 to V-1, and E edges, find the level
of node labeled as X.

Level is the minimum number of edges you must travel from the node 0 to some target.

If there doesn't exists such a node that is labeled as X, return -1.

Example 1:

Input:

X = 4
Output:
2
Explanation:

We can clearly see that Node 4 lies at Level 2.
Example 2:

Input:

X = 1
Output:
1
Explanation:
Node 1 lies at level 1, immediate after Node 0.
Your task:
You dont need to read input or print anything. Your task is to complete the function nodeLevel() which takes two 
integers V and X denoting the number of vertices and the node, and another adjacency list adj as input parameters and 
returns the level of Node X. If node X isn't present it returns -1.

Expected Time Complexity: O(V)
Expected Auxiliary Space: O(V)

Constraints:
2 ≤ V ≤ 104
1 ≤ E ≤ 104
0 ≤ adji, j < V
1 ≤ X < V
Graph doesn't contain multiple edges and self loops. """


#User function Template for python3
from collections import deque

class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        queue = deque([0])
        visited = [True] + [False] * (V - 1)
        
        level = -1
        
        while queue:
            level += 1
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == X: return level
                
                for child in adj[node]:
                    if not visited[child]:
                        queue.append(child)
                        visited[child] = True
                
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends