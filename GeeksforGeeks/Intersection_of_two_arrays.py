#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        
        #code here
        set_a=set(a)
        set_b=set(b)
        inter=(set_a.intersection(set_b))
        return len(inter)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob = Solution()
        
        print(ob.NumberofElementsInIntersection(a,b,n,m))
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
                
# } Driver Code Ends