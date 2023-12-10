""" Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum. You just need to return 
true/false depending upon whether there is a subarray present with 0-sum or not. Printing will be taken care by the 
driver code.

Example 1:

Input:
n = 5
arr = {4,2,-3,1,6}
Output: 
Yes
Explanation: 
2, -3, 1 is the subarray with sum 0.

Example 2:

Input:
n = 5
arr = {4,2,0,1,6}
Output: 
Yes
Explanation: 
0 is one of the element in the array so there exist a subarray with sum 0.
Your Task:
You only need to complete the function subArrayExists() that takes array and n as parameters and returns true or false.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= n <= 104
-105 <= a[i] <= 105 """


#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        if n == 0:
            return False
        if n == 1 and arr[0] <0:
            return False
        setofnum = set()
        sums = 0
        for i in range(n):
            sums +=arr[i]
            if sums == 0 or sums in setofnum:
                return True
            setofnum.add(sums)
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends