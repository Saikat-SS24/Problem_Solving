""" Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 
Constraints:

1 <= s.length <= 104
s consists of lowercase English letters. """
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        occurrences = {}
        visited = set()
        for i, c in enumerate(s):
            occurrences[c] = i
        stack = []
        for i, c in enumerate(s):
            if c not in visited:
                while stack and occurrences[stack[-1]] > i and stack[-1] > c:
                    visited.remove(stack.pop())
                stack.append(c)
                visited.add(c)
        return "".join(stack)

