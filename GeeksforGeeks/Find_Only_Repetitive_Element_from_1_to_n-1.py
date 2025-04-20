""" Given an array arr[] of size n, filled with numbers from 1 to n-1 in random order. The array has only one 
repetitive element. Your task is to find the repetitive element.

Note: It is guaranteed that there is a repeating element present in the array.

Examples:

Input: arr[] = [1, 3, 2, 3, 4]
Output: 3 
Explanation: The number 3 is the only repeating element.

Input: arr[] = [1, 5, 1, 2, 3, 4]
Output: 1  
Explanation: The number 1 is the only repeating element.

Input: arr[] = [1, 1]  
Output: 1
Explanation: The array is of size 2 with both elements being 1, making 1 the repeating element.

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ n-1  """

#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        #code here
        n = len(arr)
        arr.sort()
        for i in range(n-1):
            if arr[i] == arr[i+1]:
                return arr[i]
                
        return -1

    
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends