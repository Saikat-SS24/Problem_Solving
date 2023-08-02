# Given a 2D binary matrix A(0-based index) of dimensions NxM. Find the minimum number of steps required
# to reach from (0,0) to (X, Y).

# Example 1:

# Input:
# N=3, M=4
# A=[[1,0,0,0], 
#   [1,1,0,1],
#   [0,1,1,1]]
# X=2, Y=3 
# Output:
# 5
# Explanation:
# The shortest path is as follows:
# (0,0)->(1,0)->(1,1)->(2,1)->(2,2)->(2,3).

# Example 2:

# Input:
# N=3, M=4
# A=[[1,1,1,1],
#   [0,0,0,1],
#   [0,0,0,1]]
# X=0, Y=3
# Output:
# 3
# Explanation:
# The shortest path is as follows:
# (0,0)->(0,1)->(0,2)->(0,3).

#User function Template for python3
from collections import deque

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        if not A[0][0]:
            return -1
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        q=deque([(0,0)])
        count=0
        while q:
            for _ in range(len(q)):
                x,y=q.popleft()
                if (x,y)==(X,Y):
                    return count
                for i,j in dir:
                    nx,ny=x+i,y+j
                    if 0<=nx<N and 0<=ny<M and A[nx][ny]:
                        q.append((nx,ny))
                        A[nx][ny]=0
            count+=1
        
        return -1    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends