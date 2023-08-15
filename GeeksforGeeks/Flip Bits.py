""" Given an array A[] consisting of 0’s and 1’s. A flip operation is one in which you turn 1 into 0 and a 0 into 1. You have to do at most one “Flip” operation of any subarray. Formally, select a range (l, r) in the array A[], such that (0 ≤ l ≤ r < n) holds and flip the elements in this range to get the maximum ones in the final array. You can possibly make zero operations to get the answer.

Example 1:

Input:
N = 5
A[] = {1, 0, 0, 1, 0} 
Output:
4
Explanation:
We can perform a flip operation in the range [1,2]
After flip operation array is : [ 1 1 1 1 0 ]
Count of one after fliping is : 4
[Note: the subarray marked in bold is the flipped subarray]
Example 2:

Input:
N = 7
A[] = {1, 0, 0, 1, 0, 0, 1}
Output:
6
Explanation:
We can perform a flip operation in the range [1,5]
After flip operation array is : [ 1 1 1 0 1 1 1]
Count of one after fliping is : 6
[Note: the subarray marked in bold is the flipped subarray] """

#User function Template for python3

class Solution:
    def maxOnes(self, a, n):
        # Your code goes here
        count = 0
        ans = 0
        for e in a:
            if e == 0:
                count += 1
            else:
                count -= 1
            count = max(0, count)
            ans = max(ans, count)
        return sum(a)+ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.maxOnes(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends