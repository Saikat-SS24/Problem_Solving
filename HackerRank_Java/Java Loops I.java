import java.util.*;
import java.io.*;
import java.math.*;

class Solution
{
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        for(int i = 1; i <= 10; i++)
        {
            System.out.printf("%d x %d = %d%n", n, i, n*i);           
        }
        
    }
}
