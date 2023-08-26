""" Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.

Example 1:

Input:
S = "aabacbebebe", K = 3
Output: 
7
Explanation: 
"cbebebe" is the longest substring with 3 distinct characters.
Example 2:

Input: 
S = "aaaa", K = 2
Output: -1
Explanation: 
There's no substring with 2 distinct characters.
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestKSubstr() which takes the string S and an integer K as input and returns the length of the longest substring with exactly K distinct characters. If there is no substring with exactly K distinct characters then return -1.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).

Constraints:
1 ≤ |S| ≤ 105
1 ≤ K ≤ 26
All characters are lowercase latin characters. """


#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        map = {}
        # Initialize two pointers i and j to -1
        i = -1
        j = -1
        # Initialize ans to -1
        ans = -1
     
        # Loop until break statement is reached
        while True:
            # Initialize two flags to False
            flag1 = False
            flag2 = False
     
            # Loop until i reaches end of string S
            while i < len(s) - 1:
                # Set flag1 to True
                flag1 = True
                # Increment i and get character at index i
                i += 1
                ch = s[i]
                # Add character count to dictionary
                map[ch] = map.get(ch, 0) + 1
     
                # If number of unique characters is less than k, continue loop
                if len(map) < k:
                    continue
                # If number of unique characters is equal to k, update ans if necessary and continue loop
                elif len(map) == k:
                    len_ = i - j
                    ans = max(len_, ans)
                # If number of unique characters is greater than k, break loop
                else:
                    break
     
            # Loop until j reaches i
            while j < i:
                # Set flag2 to True
                flag2 = True
                # Increment j and get character at index j
                j += 1
                ch = s[j]
     
                # If character count is 1, remove character from dictionary
                if map[ch] == 1:
                    del map[ch]
                # If character count is greater than 1, decrement character
                # count in dictionary
                else:
                    map[ch] -= 1
     
                # If number of unique characters is equal to k,
                # update ans if necessary and break loop
                if len(map) == k:
                    len_ = i - j
                    ans = max(ans, len_)
                    break
                # If number of unique characters is greater than k, continue loop
                elif len(map) > k:
                    continue
     
            # If both flags are False, break outer loop (while True)
            if not flag1 and not flag2:
                break
     
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends