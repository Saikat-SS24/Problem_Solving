""" Given an array of N integers. Your task is to print the sum of all of the integers.

Example 1:

Input:
4
1 2 3 4
Output:
10
 
Example 2:

Input:
6
5 8 3 10 22 45
Output:
93
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getSum() which takes the 
array A[] and its size N as inputs and returns the sum of array in a new line.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 106
0 ≤ Arr[i] ≤ 200 """

#User function Template for python3

class Solution:
    def getSum(self, arr, n):
        # Your code goes here
        sum = 0
        for i in range(n):
            sum += arr[i]
            
        return sum
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.getSum(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends