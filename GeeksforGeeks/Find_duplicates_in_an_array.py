class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	ele=[]
    	arr.sort()
    	for i in range(1,n):
    	    if(arr[i]==arr[i-1]):
    	        ele.append(arr[i])
    	ele=list(set(ele))
    	ele.sort()
    	return ele if len(ele)>0 else[-1]

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends