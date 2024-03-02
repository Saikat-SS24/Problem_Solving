""" Given an array of n integers. Find the first element that occurs atleast k number of times.

Example 1:

Input :
n = 7, k = 2
a[] = {1, 7, 4, 3, 4, 8, 7}
Output :
4
Explanation :
Both 7 and 4 occur 2 times. But 4 is first that occurs twice.
As at index = 4, 4 has occurred twice whereas 7 appeared twice
at index 6.

Example 2:

Input :
n = 10, k = 3
a[] = {3, 1, 3, 4, 5, 1, 3, 3, 5, 4}
Output :
3
Explanation :
Here, 3 is the only number that appeared 3 times in the array.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function firstElementKTime() which takes 
the array a[], its size n, and an integer k as input arguments and returns the required answer. If the answer is not 
present in the array, return -1.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= n <= 104
1 <= k <= 100
1<= a[i] <= 200 """

#User function Template for python3


class Solution:
    def firstElementKTime(self, n, k, a):
        # code here
        d = {}
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            if d[i] >= k:
                return i
        return -1
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(n, k, a))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends