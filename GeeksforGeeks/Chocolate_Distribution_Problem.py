""" Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates
in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute 
chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of 
chocolates given to a student is minimum.

Example 1:

Input:
N = 8, M = 5
A = {3, 4, 1, 9, 56, 7, 9, 12}
Output: 6
Explanation: The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 by 
choosing following M packets :{3, 4, 9, 7, 9}.

Example 2:

Input:
N = 7, M = 3
A = {7, 3, 2, 4, 9, 12, 56}
Output: 2
Explanation: The minimum difference between maximum chocolates and minimum chocolates is 4 - 2 = 2 by 
choosing following M packets :{3, 2, 4}. """

#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        # if there are no choclates or number of student is 0
        if(M==0 or N==0):
            return 0
        # sort the given array
        A.sort()
        # number of students can't be more than number of packets
        if(N<M):
            return -1
        # largest number of choclates
        min_diff=A[N-1]-A[0]
        # find the subarray of size m such that 
        # difference between last(maximum in case sorted)
        # and first (minimum in case of sorted) elements
        # of subarray is minimum
        for i in range(len(A)-M+1):
            min_diff=min(min_diff, A[i+M-1]-A[i])
            
        return min_diff


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends