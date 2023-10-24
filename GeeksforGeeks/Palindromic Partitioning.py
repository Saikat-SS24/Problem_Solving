""" Given a string str, a partitioning of the string is a palindrome partitioning if every sub-string of the partition
is a palindrome. Determine the fewest cuts needed for palindrome partitioning of the given string.

Example 1:

Input: str = "ababbbabbababa"
Output: 3
Explaination: After 3 partitioning substrings 
are "a", "babbbab", "b", "ababa".
Example 2:

Input: str = "aaabba"
Output: 1
Explaination: The substrings after 1
partitioning are "aa" and "abba".

Your Task:
You do not need to read input or print anything, Your task is to complete the function palindromicPartition() which 
takes the string str as the input parameter and returns the minimum number of partitions required.

Expected Time Complexity: O(n*n) [n is the length of the string str]
Expected Auxiliary Space: O(n*n)

Constraints:
1 ≤ length of str ≤ 500 """


#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        # code here
        n = len(string)
        cuts = [0] * n
        
        def is_palindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
            
        for i in range(n):
            min_cuts = i  
            
            for j in range(i, -1, -1):
                if is_palindrome(string, j, i):
                    if j == 0:
                        min_cuts = 0
                    else:
                        min_cuts = min(min_cuts, 1 + cuts[j - 1])
        
            cuts[i] = min_cuts

        return cuts[n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends