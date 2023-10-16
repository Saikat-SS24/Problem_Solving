/* For a given array of price of items,you have to calculate the average of all prices upto 2 decimal places.
Note: Sum is printed automatically, you only need to calculate and return the average

Example 1:

Input:
5
1 2 3 4 5
Output:
15 3.00 
Explanation:
Sum of the array is 15, hence 
average is 15/5=3.00. 

Example 2:

Input:
9
2 55 85 656 52 554 545 5 2
Output:
1956 217.33 
Explanation:
Sum of the array is 1956, hence 
average is 1956/9= 217.33. 
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function average() which takes the array 
A[] and  its size N as inputs and returns the average of all the items as a String.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1<=N<=100
1<=Pi<=1000 */

//{ Driver Code Starts

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
class GFG{
    public static void main (String[] args) throws NumberFormatException, IOException {
    	BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine());
		String str;
		String st[];
		
            
            while(t>0)
            {
            	int N = Integer.parseInt(br.readLine());
            	int sum = 0;
            	
            	int A[] = new int[N];
            	str = br.readLine();
    			st = str.split(" ");
            	for (int i = 0; i < N; i++)
    			{
    				A[i]= Integer.parseInt(st[i]);
    				sum+=A[i];
    			}
    			Compute ob = new Compute();
            	String s=ob.average(A, N);
            	System.out.println(sum+" "+s);
                t--;
            }
    }
}

// } Driver Code Ends


class Compute
{
    String average(int A[], int N)
    {
        int sum = 0;
        for(int i = 0; i<N; i++){
            sum = sum+A[i];
        }
        double res = (double)sum / N;
        String format = String.format("%.2f", res);
        return format;
    }
}
