/* Given two numbers A and B. Your task is to return the sum of A and B.

Example 1:

Input:
A = 1, B = 2
Output:
3
Explanation:
Addition of 1 and 2 is 3.
 

Example 2:

Input:
A = 10, B = 20
Output:
30
Explanation:
Addition os 10 and 20 is 30.
 
Your Task:

You don't need to read input or print anything. Your task is to complete the function addition() which takes two numbers
A and B and returns the sum of A and B.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
1 <= A, B <= 1018 */

//{ Driver Code Starts
//Initial Template for Java
import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            String[] inp=read.readLine().split(" ");
            int A=Integer.parseInt(inp[0]);
            int B=Integer.parseInt(inp[1]);
            Solution ob = new Solution();
            System.out.println(ob.addition(A,B));
        }
    }
}

// } Driver Code Ends


//User function Template for Java
class Solution{
    static int addition(int A, int B){
        // code here
        return A+B;
    }
} 