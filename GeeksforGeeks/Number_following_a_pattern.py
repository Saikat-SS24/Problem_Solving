""" Given a pattern containing only I's and D's. I for increasing and D for decreasing. Devise an algorithm to print 
the minimum number following that pattern. Digits from 1-9 and digits can't repeat.

Example 1:

Input:
D
Output:
21
Explanation:
D is meant for decreasing, so we choose the minimum number among all possible numbers like 21,31,54,87,etc.

Example 2:

Input:
IIDDD
Output:
126543
Explanation:
Above example is self- explanatory,
1 < 2 < 6 > 5 > 4 > 3
  I - I - D - D - D
Your Task:

You don't need to read input or print anything. Your task is to complete the function printMinNumberForPattern() which
takes the string S and returns a string containing the minimum number following the valid number.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ Length of String ≤ 8 """



#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        result = []
        stack = []
        num = 1
        for c in S:
            if c == "D":
                stack.append(num)
                num += 1
            else:
                stack.append(num)
                num += 1
                # convert to str and reverse stack
                # add to result and clean
                result += [str(i) for i in stack][::-1]
                stack = []
                
        stack.append(num)
        result += [str(i) for i in stack][::-1]
            
        return int(''.join(result))


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends