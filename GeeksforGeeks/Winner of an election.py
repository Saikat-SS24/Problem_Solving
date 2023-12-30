""" Given an array of n names arr of candidates in an election, where each name is a string of lowercase characters. 
A candidate name in the array represents a vote casted to the candidate. Print the name of the candidate that received 
the maximum count of votes. If there is a draw between two candidates, then print lexicographically smaller name.

Example 1:

Input:
n = 13
arr[] = {john,johnny,jackie,johnny,john 
jackie,jamie,jamie,john,johnny,jamie,
johnny,john}
Output: john 4
Explanation: john has 4 votes casted for 
him, but so does johny. john is 
lexicographically smaller, so we print 
john and the votes he received.

Example 2:

Input:
n = 3
arr[] = {andy,blake,clark}
Output: andy 1
Explanation: All the candidates get 1 
votes each. We print andy as it is 
lexicographically smaller.
Your Task:
You only need to complete the function winner() that takes an array of strings arr, and length of arr n as parameters 
and returns an array of string of length 2. First element of the array should be the name of the candidate and second 
element should be the number of votes that candidate got in string format.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= n <= 105
1 <= |arri| <= 105 """


#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        d = {}
        res = 0
        for i in arr:
            if(i in d):
                d[i] += 1
                res = max(res,d[i])
            else:
                d[i] = 1
                res = max(res,d[i])
        ans = []
        for i in d:
            if(d[i] == res):
                ans.append(i)
        if(len(ans) == 1):
            return [ans[-1],str(res)]
        else:
            ans.sort()
            return [ans[0],str(res)]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])


# } Driver Code Ends