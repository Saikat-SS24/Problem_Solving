"""Print numbers from 1 to N without the help of loops.

Example 1:

Input:
N = 10
Output: 1 2 3 4 5 6 7 8 9 10

Example 2:

Input:
N = 5
Output: 1 2 3 4 5
 
Your Task:
This is a function problem. You only need to complete the function printNos() that takes N as parameter and prints 
number from 1 to N recursively. Don't print newline, it will be added by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).

Constraints:
1 <= N <= 1000 """

#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        self.N=N
        if N > 0:
            self.printNos(N - 1)
            print(N,end=" ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        ob=Solution()
        
        ob.printNos(N)
        print()
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends