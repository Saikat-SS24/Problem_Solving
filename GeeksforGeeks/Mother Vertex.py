""" Given a Directed Graph, find a Mother Vertex in the Graph (if present). 
A Mother Vertex is a vertex through which we can reach all the other vertices of the Graph.

Example 1:

Input: 

Output: 0
Explanation: According to the given edges, all 
nodes can be reaced from nodes from 0, 1 and 2. 
But, since 0 is minimum among 0,1 and 2, so 0 
is the output.
Example 2:

Input: 

Output: -1
Explanation: According to the given edges, 
no vertices are there from where we can 
reach all vertices. So, output is -1.
Your Task:
You don't need to read or print anything. Your task is to complete the function findMotherVertex() which takes V denoting the number of vertices and adjacency list as imput parameter and returns the verticex from through which we can traverse all other vertices of the graph. If there is more than one possible nodes then returns the node with minimum value.If not possible returns -1.

Expected Time Complexity: O(V + E)
Expected Space Compelxity: O(V)

Constraints:
1 ≤ V ≤ 500 """


class Solution:
    
    #Function to find a Mother Vertex in the Graph.
	def findMotherVertex(self, V, adj):
		#Code here
		visited = [False]* V
        last_visited = None
        
        for vertex in range(V):
            if not visited[vertex]:
                self.dfs(vertex, adj, visited)
                last_visited = vertex
                
        visited = [False]* V
        self.dfs(last_visited, adj, visited)
        
        for vertex in range(V):
            if not visited[vertex]:
                return -1
        return last_visited
        
    def dfs(self, s, adj, visited):
        visited[s] = True
        for neighbor in adj[s]:
            if not visited[neighbor]:
                self.dfs(neighbor, adj, visited)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends