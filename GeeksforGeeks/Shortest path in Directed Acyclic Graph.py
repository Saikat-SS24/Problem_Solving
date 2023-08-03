# Given a Directed Acyclic Graph of N vertices from 0 to N-1 and a 2D Integer array(or vector) 
# edges[ ][ ] of length M, where there is a directed edge from edge[i][0] to edge[i][1] with 
# a distance of edge[i][2] for all i.

# Find the shortest path from src(0) vertex to all the vertices and if it is impossible to reach any vertex, 
# then return -1 for that vertex.
    
# Example1:

# Input:
# N = 4, M = 2
# edge = [[0,1,2],[0,2,1]
# Output:
# 0 2 1 -1
# Explanation:
# Shortest path from 0 to 1 is 0->1 with edge weight 2. 
# Shortest path from 0 to 2 is 0->2 with edge weight 1.
# There is no way we can reach 3, so it's -1 for 3.
# Example2:

# Input:
# N = 6, M = 7
# edge = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
# Output:
# 0 2 3 6 1 5
# Explanation:
# Shortest path from 0 to 1 is 0->1 with edge weight 2. 
# Shortest path from 0 to 2 is 0->4->2 with edge weight 1+2=3.
# Shortest path from 0 to 3 is 0->4->5->3 with edge weight 1+4+1=6.
# Shortest path from 0 to 4 is 0->4 with edge weight 1.
# Shortest path from 0 to 5 is 0->4->5 with edge weight 1+4=5.


#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        from heapq import heappush, heappop
        from collections import defaultdict
        
        g = defaultdict(list)
        for frm, to, cost in edges:
            g[frm].append((to, cost))

        costs = [-1]*n
        costs[0] = 0

        q = [(0, 0)]
        while q:
            cost0, v = heappop(q)
            for to, dc in g[v]:
                cost = cost0+dc
                if costs[to] == -1 or costs[to] > cost:
                    heappush(q, (cost, to))
                    costs[to] = cost
        return costs


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




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



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends