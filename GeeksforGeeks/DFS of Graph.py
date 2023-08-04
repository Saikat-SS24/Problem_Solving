""" You are given a connected undirected graph. Perform a Depth First Traversal of the graph.

Example 1:

Input: V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]

     0
   / | \
  2  3  1
  |
  4

Output: 0 2 4 3 1
Explanation: 
0 is connected to 2, 3, 1.
1 is connected to 0.
2 is connected to 0 and 4.
3 is connected to 0.
4 is connected to 2.
so starting from 0, it will go to 2 then 4,
and then 3 and 1.
Thus dfs will be 0 2 4 3 1.

Example 2:

Input: V = 4, adj = [[1,3], [2,0], [1], [0]]

    0
   / \
  1   3
  \
   2
Output: 0 1 2 3
Explanation:
is connected to 1 , 3.
1 is connected to 0, 2. 
2 is connected to 1.
3 is connected to 0. 
so starting from 0, it will go to 1 then 2
then back to 0 then 0 to 3
thus dfs will be 0 1 2 3. """


#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        def dfs(i,adj,visited,ans):
            visited[i]=True
            ans.append(i)
            for j in adj[i]:
                if (visited[j]==False):
                    dfs(j,adj,visited,ans)
        ans=[]
        visited=[False]*V
        dfs(0,adj,visited,ans)
        return ans


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends