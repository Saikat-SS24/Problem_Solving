""" Given a number n, the task is to find out whether this number is a Smith number or not. A Smith number is a 
composite number whose sum of digits is equal to the sum of digits of its prime factors.

Example 1:

Input:
n = 4
Output:
1
Explanation:
The sum of the digits of 4 is 4, and the sum of the digits of its prime factors is 2 + 2 = 4.

Example 2:

Input:
n = 378
Output:
1
Explanation:
378 = 21*33*71 is a Smith number since 3+7+8 = 2*1+3*3+7*1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function smithNum() which takes an Integer 
n as input and returns the answer.

Expected Time Complexity: O(n * log(n))
Expected Auxiliary Space: O(n)

Constraints:
1 <= n <= 105 """

#User function Template for python3

class Solution:
    def smithNum(self, n):
        # code here 
        def sum_digits(num):
            return sum(int(digit) for digit in str(num))

        def sum_prime_factor(num):
            s = 0
            i = 2
            M = num
            while i <= num:
                if num%i == 0 and i != M:
                    s += sum_digits(i)
                    num //= i
                else:
                    i += 1
            return s
    
        return int(sum_digits(n) == sum_prime_factor(n))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends