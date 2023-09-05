"""Given an undirected graph with V nodes and E edges, create and return an adjacency list of the graph. 
0-based indexing is followed everywhere.

Example 1:

Input:
V = 5, E = 7
edges = {(0,1),(0,4),(4,1),(4,3),(1,3),(1,2),(3,2)}

Output: 
{{1,4}, 
 {0,2,3,4}, 
 {1,3},
 {1,2,4},
 {0,1,3}}
Explanation:
Node 0 is connected to 1 and 4.
Node 1 is connected to 0,2,3 and 4.
Node 2 is connected to 1 and 3.
Node 3 is connected to 1,2 and 4.
Node 4 is connected to 0,1 and 3.

Example 2:

Input:
V = 4, E = 3
edges = {(0,3),(0,2),(2,1)}

Output: 
{{2,3} 
 {2}, 
 {0,1} 
 {0}}
Explanation:
Node 0 is connected to 2 and 3.
Node 1 is only connected to 2.
Node 2 is connected to 0 and 1.
Node 3 is only connected to 0.
Your task:
You don't need to read input or print anything. Your task is to complete the function printGraph() which takes the integer V denoting the number of vertices and edges as input parameters and returns the list of list denoting the adjacency list.

Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V + E)

Constraints:
1 ≤ V, E ≤ 105 """


from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        adj = [set() for i in range(V)]
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        for i in range(V):
            adj[i] = list(adj[i])
        return adj

#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        V,E=IntArray().Input()
        
        
        edges=IntMatrix().Input(E, 2)
        
        obj = Solution()
        res = obj.printGraph(V, edges)
        
        for row in res:
            print(*sorted(row))
# } Driver Code Ends