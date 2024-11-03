""" Given an undirected graph with no self loops with V (from 0 to V-1) nodes and E edges, the task is to check if 
there is any cycle in the undirected graph.

Note: Solve the problem using disjoint set union (DSU).

Example 1:

Input: 

1   0
 \ /| \
  3 |  4
    2 /

Output: 1
Explanation: There is a cycle between 0->2->4->0

Example 2:

Input:

1   0 
 \ /| 
  3 |  4
    2 /

Output: 0
Explanation: The graph doesn't contain any cycle
Your Task:
You don't need to read or print anyhting. Your task is to complete the function detectCycle() which takes number of 
vertices in the graph denoting as V and adjacency list adj and returns 1 if graph contains any cycle otherwise returns 
0.

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)

Constraints:
2 ≤ V ≤ 104
1 ≤ E ≤ 104 """


class Solution:

    #Function to detect cycle using DSU in an undirected graph.
	def detectCycle(self, V, adj):
		#Code here
		parent = list(range(V))
		rank = [1] * V
        	
        def find(u):
            root = u
            while root != parent[root]:
                root = parent[root]
            # Updating the path
            while u != root:
                u, parent[u] = parent[u], root
            return root
        
        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if u_root == v_root:
                return u_root
            # Make sure u_root points to the bigger set
            if rank[u_root] < rank[v_root]:
                u_root, v_root = v_root, u_root
            parent[v_root] = u_root
            rank[u_root] += rank[v_root]
            return u_root
        
        for u in range(V):
            # Edges might repeat in the adjacency list
            # using set() to eliminate the duplicates.
            for v in set(adj[u]):
                if v < u:
                    continue
                u_root = find(u)
                v_root = find(v)
                if u_root == v_root:
                    return 1
                union(u_root, v_root)
        
        return 0

#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.detectCycle(V, adj)
		print(ans)
# } Driver Code Ends