/* Given a positive integer N, determine whether it is odd or even.

Example 1:

Input:
N = 1
Output:
odd
Explanation:
The output is self-
explanatory.
 
Example 2:

Input:
N = 2
Output:
even
Explanation:
The output is self-
explanatory.
 
Your Task:

You don't need to read input or print anything. Your task is to complete the function oddEven() which takes the integer
N and return "even" is number is even and "odd" if the number is odd.

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
0 <= N <= 10000 */

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
            int N = Integer.parseInt(read.readLine());

            Solution ob = new Solution();
            System.out.println(ob.oddEven(N));
        }
    }
}
// } Driver Code Ends

//User function Template for Java
class Solution{
    static String oddEven(int N){
        // code here
        if(N%2 == 1){
            return "odd";
        }else{
            return "even";
        }
    }
}