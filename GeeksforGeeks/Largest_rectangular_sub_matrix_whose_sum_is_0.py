""" Given a matrix mat[][] of size N x M. The task is to find the largest rectangular sub-matrix by area whose sum is 0.

If there are multiple solutions return the rectangle which starts from minimum column index. If you still have multiple 
solutions return the one starting from minimum row index. If you still have multiple solutions return the one having 
greatest row number. If no such matrix is present return a zero (0) size matrix.

Example 1:

Input: N = 3, M = 3
mat[][] =  1, 2, 3
          -3,-2,-1
           1, 7, 5

Output:  1, 2, 3
        -3,-2,-1

Explanation: This is the largest sub-matrix,
whose sum is 0.

Example 2:

Input: N = 4, M = 4
mat[][] = 9, 7, 16, 5
          1,-6,-7, 3
          1, 8, 7, 9
          7, -2, 0, 10

 Output: -6,-7
          8, 7
         -2, 0 
Your Task:
You don't need to read input or print anything. You just have to complete the function sumZeroMatrix() which takes a 2D 
matrix mat[][], its dimensions N and M as inputs and returns a largest sub-matrix, whose sum is 0.

Expected Time Complexity: O(N*M*M).
Expected Auxiliary Space: O(N*M).


Constraints:
1 <= N, M <= 100
-1000 <= mat[][] <= 1000 """


from typing import List


from typing import List


class Solution:
    def sumZeroMatrix(self, a : List[List[int]]) -> List[List[int]]:
        # code here
        m,n=len(a),len(a[0])
        pre_sum=[[0]*(n+1) for _ in range(m+1)]
        def solve(arr):
            mp={0:-1}
            ssum=0
            l,r=-1,-1
            for i,val in enumerate(arr):
                ssum=ssum+val
                if ssum in mp:
                    ll,rr=mp[ssum],i
                    if rr-ll>r-l:
                        l,r=ll,rr
                else:
                    mp[ssum]=i
            return l+1,r
        for i in range(1,m+1):
            for j in range(1,n+1):
                pre_sum[i][j]=pre_sum[i][j-1]+a[i-1][j-1]
        lr,rr,lc,rc,ans=-1,-1,-1,-1,0
        for c1 in range(1,n+1):
            for c2 in range(c1,n+1):
                arr=[]
                for i in range(1,m+1):
                    arr.append(pre_sum[i][c2]-pre_sum[i][c1-1])
                l,r=solve(arr)
                if l==r==-1: continue
                if (r-l+1)*(c2-c1+1)>ans:
                    lr,rr=l,r
                    lc,rc=c1-1,c2-1
                    ans=(r-l+1)*(c2-c1+1)
                elif (r-l+1)*(c2-c1+1)==ans and lc==c1:
                    if l<lr:
                        lr,rr=l,r
                        lc,rc=c1-1,c2-1
                        ans=(r-l+1)*(c2-c1+1)
                    elif l==lr and r>rr:
                        lr,rr=l,r
                        lc,rc=c1-1,c2-1
                        ans=(r-l+1)*(c2-c1+1)
        ret=[] 
        if ans==0:
            return ret
        for i in range(lr,rr+1):
            tt=[]
            for j in range(lc,rc+1):
                tt.append(a[i][j])
            ret.append(tt)
        return ret



#{ 
 # Driver Code Starts

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
        
        nm=IntArray().Input(2)
        
        
        a=IntMatrix().Input(nm[0], nm[1])
        
        obj = Solution()
        res = obj.sumZeroMatrix(a)
        if len(res) == 0:
            print(-1)
        else:
            IntMatrix().Print(res)    

# } Driver Code Ends