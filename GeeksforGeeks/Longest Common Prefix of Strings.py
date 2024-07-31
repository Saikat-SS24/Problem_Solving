""" Given an array of strings arr. Return the longest common prefix among all strings present in the array. 
If there's no prefix common in all the strings, return "-1".

Examples :

Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
Output: gee
Explanation: "gee" is the longest common prefix in all the given strings.

Input: arr[] = ["hello", "world"]
Output: -1
Explanation: There's no common prefix in the given strings.

Expected Time Complexity: O(n*min(|arri|))
Expected Space Complexity: O(min(|arri|))

Constraints:
1 ≤ |arr| ≤ 103
1 ≤ |arr[i]| ≤ 103  """

#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        res = arr[0]
        length = len(res)
        # Iterate for the rest of the elements in the array
        for i in range(1, len(arr)):
            # Find the index of result in the current string
            while arr[i].find(res) != 0:
                # Update the matched substring prefix
                res = res[:length - 1]
                length -= 1

                # Check for an empty case and return if true
                if not res:
                    return "-1"

        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends