""" Given an array of n integers. Find the minimum non-negative number to be inserted in array, so that sum of all 
elements of array becomes prime.

Example 1:

Input:
N=5
arr = {2, 4, 6, 8, 12}
Output:  
5
Explanation: 
The sum of the array is 32 ,we can add 5 to this to make it 37 which is a prime number.

Example 2:

Input:
N=3
arr = {1, 5, 7}
Output:  
0 
Explanation: 
The sum of the array is 13 which is already prime. 
Your Task:
You don't need to read input or print anything. Your task is to complete the function minNumber() that takes array 
arr and integer N as input parameters and returns the minimum positive number to be inserted in the array so as to make 
it's sum a prime number.

Expected Time Complexity: O(N log(log N))
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 105
1 ≤ sum of all elements ≤ 106 """


#User function Template for python3



class Solution:
    def minNumber(self, arr,n):
        # code here
        def checkPrime(N):
            if N>1:
                for i in range(2,int(N**0.5)+1):
                    if N%i==0:
                        return False
                return True
            else:
                return False
        i=0
        ans=sum(arr)
        while True:
            if checkPrime(ans+i):
               return i
            i+=1

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends