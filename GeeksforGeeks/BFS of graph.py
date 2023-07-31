# Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.

# Example 1:

# Input:

#   0
#  / \  \
# 1   2  \ 
#     /   3
#    4

# Output: 0 1 2 3 4
# Explanation: 
# 0 is connected to 1 , 2 , 3.
# 2 is connected to 4.
# so starting from 0, it will go to 1 then 2
# then 3. After this 2 to 4, thus bfs will be
# 0 1 2 3 4.

# Example 2:

# Input:

#    0
#   / \
#  1   2

# Output: 0 1 2
# Explanation:
# 0 is connected to 1 , 2.
# so starting from 0, it will go to 1 then 2,
# thus bfs will be 0 1 2. 

#User function Template for python3

from typing import List
from queue import Queue
from collections import deque

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q=deque([])
        q.append(0)
        vis=[0]*(V)
        vis[0]=1
        list=[]
        while(len(q)!=0):
            cur=q.popleft()
            list.append(cur)
            for i in adj[cur]:
                if(vis[i]==0):
                    q.append(i)
                    vis[i]=1
        return list


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends
