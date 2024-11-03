""" Given an integer array arr of size n, you need to sum the elements of arr.

Example 1:

Input:
n = 3
arr[] = {3 2 1}
Output: 6
Example 2:

Input:
n = 4
arr[] = {1 2 3 4}
Output: 10
Your Task:
You need to complete the function sumElement() that takes arr and n and returns the sum. The printing is done by the 
driver code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n <= 103
1 <= arri <= 104 """

#User function Template for python3

def sumElement(arr,n):
    #code here
    sum = 0
    for i in range(0,len(arr)):
        sum = sum+arr[i]
        
    return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    testCase=int(input())
    
    for _ in range(testCase):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(sumElement(arr,n))
# } Driver Code Ends