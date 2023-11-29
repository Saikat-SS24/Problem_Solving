""" An Eulerian Path is a path in graph that visits every edge exactly once and it starts and ends up at different 
indexes. An Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex. Given an undirected acyclic 
graph with V nodes, and E edges, with adjacency list adj, return 2 if the graph contains an eulerian circuit, else if 
the graph contains an eulerian path, return 1, otherwise, return 0.

Example 1:

Input: 

       0
      / \
     1---2

Output: 2
Explanation: 
Following is an eulerian circuit in the mentioned graph
1 -> 2 -> 0 -> 1

Example 2:

Input: 

      0
     / \
    1   2

Output: 1
Explanation: 
Following is an eulerian circuit in the mentioned graph
1 -> 0 -> 2
Your Task:
You don't need to read or print anything. Your task is to complete the function isEulerCircuilt() which takes number of 
vertices in the graph denoted as V and an adjacency list of graph denoted as adj and returns 2 if the graph contains 
an eulerian circuit, else if the graph contains an eulerian path, it returns 1, otherwise, it will return 0.

Expected Time Complexity: O(V+E) where E is the number of edges in graph.
Expected Space Complexity: O(V)

Constraints:
1 ≤ V, E ≤ 104
1 ≤ adj[i][j] ≤ V-1 """


class Solution:
	def isEulerCircuitExist(self, V, adj):
		#Code here
		degree = [0]*V
        
        for r in adj:
            for e in r:
                degree[e] += 1
        
        cnt = sum(1  for e in degree if e%2 != 0)
        if cnt == 0:
            return 2
        if cnt <= 2:
            return 1
        return 0


#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEulerCircuitExist(V, adj)
		print(ans)
# } Driver Code Ends