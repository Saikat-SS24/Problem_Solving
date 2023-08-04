""" Given an array of size N. The task is to sort the array elements by completing functions heapify() and buildHeap() 
which are used to implement Heap Sort.

Example 1:

Input:
N = 5
arr[] = {4,1,3,9,7}
Output:
1 3 4 7 9
Explanation:
After sorting elements
using heap sort, elements will be
in order as 1,3,4,7,9.

Example 2:

Input:
N = 10
arr[] = {10,9,8,7,6,5,4,3,2,1}
Output:
1 2 3 4 5 6 7 8 9 10
Explanation:
After sorting elements
using heap sort, elements will be
in order as 1, 2,3,4,5,6,7,8,9,10. """

#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        largest = i # initialize largest as root 
        l=2*i+1     # left = 2*i+1
        r=2*i+2     # right = 2*i+2
        # see if left child of root exists and is greater than root
        if l<n and arr[largest]<arr[l]:
            largest=l
            
        # see if right child of root exists and is greater than root
        if r<n and arr[largest]<arr[r]:
            largest=r
        
        # change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] # swap
            
            # heapify the root
            self.heapify(arr, n, largest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n, -1, -1):
            self.heapify(arr,n,i)
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        for i in range(n-1,0,-1):
            arr[i],arr[0] = arr[0], arr[i] # swap
            self.heapify(arr,i,0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends