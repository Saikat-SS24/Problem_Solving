""" Given 2 sorted integer arrays arr1 and arr2. Find the sum of the middle elements of two sorted arrays 
arr1 and arr2.

Examples:

Input: arr1 = [1, 2, 4, 6, 10], arr2 = [4, 5, 6, 9, 12]
Output: 11
Explanation: The merged array looks like [1, 2, 4, 4, 5, 6, 6, 9, 10, 12]. Sum of middle elements is 11 (5 + 6).

Input: arr1 = [1, 12, 15, 26, 38], arr2 = [2, 13, 17, 30, 45]
Output: 32
Explanation: The merged array looks like [1, 2, 12, 13, 15, 17, 26, 30, 38, 45]. Sum of middle elements is 32 
(15 + 17).

Expected Time Complexity: O(log n)
Expected Auxiliary Space: O(1)

Constraints:

1 <= arr1.size() == arr2.size() <= 103
1 <= arr1[i] <= 106
1 <= arr2[i] <= 106 """

#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        n = len(arr1)
        i, j = 0, 0
        m1, m2 = -1, -1
    
        # Iterate until we reach the middle of the merged array
        for count in range(n + 1):
            # If arr1[] is exhausted, the middle elements are in arr2[]
            if i == n:
                m1 = m2
                m2 = arr2[0]
                break
            # If arr2[] is exhausted, the middle elements are in arr1[]
            elif j == n:
                m1 = m2
                m2 = arr1[0]
                break
    
            # Update m1 and m2 with the smaller current element
            if arr1[i] <= arr2[j]:
                m1 = m2
                m2 = arr1[i]
                i += 1
            else:
                m1 = m2
                m2 = arr2[j]
                j += 1
    
        # Return the sum of the middle elements
        return m1 + m2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends