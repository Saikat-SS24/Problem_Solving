""" Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

Example 1:

Input:
N = 16
A = {0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15}
Output: 
6
Explanation:
There are more than one LIS in this array. One such Longest increasing subsequence is {0,2,6,9,13,15}.
Example 2:

Input:
N = 6
A[] = {5,8,3,7,9,1}
Output: 
3
Explanation:
There are more than one LIS in this array.  One such Longest increasing subsequence is {5,7,9}. """

#User function Template for python3

class Solution:
    
    global maximum
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        list = []
        n = len(a)
        def lower_bound(v, a, n):
            l = 0
            r = n - 1
            while(l < r):
                mid = l + (r - l)//2
                if a[mid] >= v:
                    r = mid
                else:
                    l = mid + 1
            return l
        c = 0
        for i in range(n):
            if list == [] or list[-1] < a[i]:
                list.append(a[i])
                c += 1
            else:
                l = lower_bound(a[i], list, c)
                list[l] = a[i]
        return len(list)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends