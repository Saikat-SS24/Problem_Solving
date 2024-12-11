""" Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without 
using any extra space. Modify a so that it contains the first n elements and modify b so that it contains the last m 
elements.

Examples:

Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output:
2 2 3 4
7 10
Explanation: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10

Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output:
1 2 3 5 8 9
10 13 15 20
Explanation: After merging two sorted arrays we get 5 10 12 18 20.

Input: a[] = [0, 1], b[] = [2, 3]
Output:
0 1
2 3
Explanation: After merging two sorted arrays we get 0 1 2 3.

Constraints:
1 <= a.size(), b.size() <= 105
0 <= a[i], b[i] <= 107

Approach - Actually we can use the previous approach without finding the pivot index. We just need to swap the 
rightmost element in a[] with leftmost element in b[], then second rightmost element in a[] with second leftmost 
element in b[] and so on. This will continue until the selected element from a[] is larger than selected element 
from b[].
When we reach at the pivot index this condition fails automatically and we will stop here. Now sort both the arrays 
to maintain the order. """


class Solution:
    def mergeArrays(self, a, b):
        # code here
        i = len(a) - 1
        j = 0
        while i >= 0 and j < len(b):
            if a[i] < b[j]:
                i -= 1
            else:
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
                
        a.sort()
        b.sort()

#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends