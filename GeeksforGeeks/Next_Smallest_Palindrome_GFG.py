""" Given a number, in the form of an array Num[] of size N containing digits from 1 to 9(inclusive). The task is to find the next smallest palindrome strictly larger than the given number.

Example 1:

Input:
N = 11
Num[] = {9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2}
Output: 9 4 1 8 8 0 8 8 1 4 9
Explanation: Next smallest palindrome is
9 4 1 8 8 0 8 8 1 4 9
Example 2:

Input:
N = 5
Num[] = {2, 3, 5, 4, 5}
Output: 2 3 6 3 2
Explanation: Next smallest palindrome is
2 3 6 3 2
Your Task:
Complete the function generateNextPalindrome() which takes an array num, and a single integer n, as input parameters and returns an array of integers denoting the answer. You don't to print answer or take inputs.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= Num[i] <= 9 """


#User function Template for python3
class Solution:


	def generateNextPalindrome(self,num, n ) :
	    # code here
	    flag = False
        mid = (n-1)//2
        
        for i in range(mid+1,n) :
            if num[i] == num[n-i-1] : continue
            if num[i] < num[n-i-1] :
                flag = True
                break
            else :
                break
        if flag :
            for i in range(mid+1,n) :
                num[i] = num[n-i-1]
            res = [0]*n
            for i in range(n) :
                res[i] = num[i]
            return res
            
        index=-1;
        for i in range(mid,-1,-1) :
            if(num[i]<9) :
                index=i
                break
        if(index==-1):
            flag1 = False
            for i in range(mid+1,n) :
                if(num[i]!=9) :
                    flag1=True
                    break
            if(flag1) :
                res = [9]*n
                return res
            
            res = [0]*(n+1)
            res[0]=1
            res[n]=1
            return res
            
        num[index]+=1
        for i in range(index+1,mid+1) :
            num[i]=0
        
        for i in range(mid+1,n) : 
            num[i]=num[n-i-1]
            
        res = [0]*n
        for i in range(n) :
            res[i]=num[i]
        return res 




#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        num=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.generateNextPalindrome(num, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends