""" Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or 
false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 
Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000 """

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n = len(arr)
        freq = defaultdict (int)
    
        # Store the frequency of each
        # element from the array
        for i in range (n):
            freq[arr[i]] += 1
    
        uniqueFreq = set([])
        # Check whether frequency of any
        # two or more elements are same
        # or not. If yes, return false
        for i in freq:
            if (freq[i] in uniqueFreq):
                return False
            else:
                uniqueFreq.add(freq[i])
        # Return true if each
        # frequency is unique
        return True     