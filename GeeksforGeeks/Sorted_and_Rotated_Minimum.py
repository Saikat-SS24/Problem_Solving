""" A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum element 
in it. 

Examples:

Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
Explanation: 1 is the minimum element in the array.

Input: arr[] = [3, 2, 1]
Output: 1
Explanation: Here 1 is the minimum element.

Input: arr[] = [4, 2, 2]
Output: 2
Explanation: Here 2 is the only minimum element.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 109  """

#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        return min(arr)

#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends