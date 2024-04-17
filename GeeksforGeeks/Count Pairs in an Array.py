""" Given an array arr of n integers, count all pairs (arr[i], arr[j]) in it such that i*arr[i] > j*arr[j] and 
0 ≤ i < j < n.

Note: 0-based Indexing is followed.

Example 1:

Input :
n = 4
arr[] = {8, 4, 2, 1}
Output :
2
Explanation:
If we see the array after operations
[0*8, 1*4, 2*2, 3*1] => [0, 4, 4, 3]
Pairs which hold the condition i*arr[i] > j*arr[j] are (4,1) and (2,1), so in total 2 pairs are available.

Example 2:

Input :
n = 7
arr[] = {5, 0, 10, 2, 4, 1, 6}
Output:
5
Explanation :
Pairs which hold the condition i*arr[i] > j*arr[j] are (10,2), (10,4), (10,1), (2,1) and (4,1), so in total 5 pairs 
are there.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countPairs() which takes the 
array arr[] and its size n as inputs and returns the required result.

Expected Time Complexity: O(n*log(n))
Expected Auxiliary Space: O(n*log(n))

Constraints:
1 ≤ n ≤ 104
0 ≤ arr[i] ≤ 104  """


#User function Template for python3
from bisect import bisect_left

class Solution:    
    def countPairs(self,arr, n): 
        # Your code goes here
        # storing i*arr[i] for every index
        for i in range(n):
            arr[i] = i * arr[i]
     
        s = []
        ans = 0
     
        for i in range(n - 1, -1, -1):
           
            # for the last element, the count is zero, so excluding it
            if(i != n - 1):
                # add the count of smaller elements to the right of
                # the current element into the ans variable
                ans += bisect_left(s, arr[i])
     
            # insert current element
            s.insert(bisect_left(s, arr[i]), arr[i])
     
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob= Solution()
        print(ob.countPairs(a, n))

        T -= 1


if __name__ == "__main__":
    main()
    
# } Driver Code Ends