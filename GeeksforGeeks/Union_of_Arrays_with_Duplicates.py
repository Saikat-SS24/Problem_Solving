""" Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.

The Union of the two arrays can be defined as the set containing distinct elements from both arrays. If there are 
repetitions, then only one element occurrence should be there in the union.

Note: Elements of a[] and b[] are not necessarily distinct.

Examples

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3]
Output: 5
Explanation: Union set of both the arrays will be 1, 2, 3, 4 and 5. So count is 5.

Input: a[] = [85, 25, 1, 32, 54, 6], b[] = [85, 2] 
Output: 7
Explanation: Union set of both the arrays will be 85, 25, 1, 32, 54, 6, and 2. So count is 7.

Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
Output: 2
Explanation: We need to consider only distinct. So count of elements in union set will be 2.

Constraints:
1 ≤ a.size(), b.size() ≤ 106
0 ≤ a[i], b[i] ≤ 105  """


#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        s = set()
        for i in a:
            s.add(i)
        for i in b:
            s.add(i)
            
        return len(s)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.findUnion(a, b))
        print("~")

# } Driver Code Ends