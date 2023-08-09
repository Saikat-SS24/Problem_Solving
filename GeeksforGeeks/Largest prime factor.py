""" Given a number N, the task is to find the largest prime factor of that number.
 Example 1:

Input:
N = 5
Output:
5
Explanation:
5 has 1 prime factor i.e 5 only.
Example 2:

Input:
N = 24
Output:
3
Explanation:
24 has 2 prime factors 2 and 3 in which 3 is greater. """


#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
        # code here
        prime_factors_list=[]
        i=2
        while i*i<=N:
            if N%i:
                i+=1
            else:
                N//=i
                prime_factors_list.append(i)
        if N>1:
            prime_factors_list.append(N)
        
        largest_prime_factor=max(prime_factors_list)
        return largest_prime_factor
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends