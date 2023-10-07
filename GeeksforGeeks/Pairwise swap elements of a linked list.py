""" Given a singly linked list of size N. The task is to swap elements in the linked list pairwise.
For example, if the input list is 1 2 3 4, the resulting list after swaps will be 2 1 4 3.
Note: You need to swap the nodes, not only the data. If only data is swapped then driver will print -1.

Example 1:

Input:
LinkedList: 1->2->2->4->5->6->7->8
Output: 
2 1 4 2 6 5 8 7
Explanation: 
After swapping each pair considering (1,2), (2, 4), (5, 6).. so on as pairs, we get 2, 1, 4, 2, 6, 5, 8, 7 as a 
new linked list.
Example 2:

Input:
LinkedList: 1->3->4->7->9->10->1
Output: 
3 1 7 4 10 9 1
Explanation: 
After swapping each pair considering (1,3), (4, 7), (9, 10).. so on as pairs, we get 3, 1, 7, 4, 10, 9, 1 as a 
new linked list.
Your Task:
The task is to complete the function pairWiseSwap() which takes the head node as the only argument and returns 
the head of modified linked list.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 105 """

"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""

# complete this function
# return head of list after swapping


class Solution:    
    def pairWiseSwap(self, head):
        # code here
        if head == None: return head
        temp, head, prev = head, None, None
        while temp != None:
            if temp.next == None:
                if head == None:
                    head = temp
                else:
                    prev.next = temp
                break
            next = temp.next.next
            if head == None:
                head = temp.next
                head.next = temp
            else:
                prev.next = temp.next
                if temp.next != None: temp.next.next = temp
            temp.next = None
            prev = temp
            temp = next
        return head
 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
            
        dict1 = {}
        temp = lis.head
        while temp:
            dict1[temp] = temp.data
            temp = temp.next
        
        failure = LinkedList()
        failure.insert(-1)
        
        head = Solution().pairWiseSwap(lis.head)
        
        temp = head
        f = 0
        while temp:
            if dict1[temp] != temp.data:
                f = 1;
            temp = temp.next
        
        if f:
            printList(failure)
        else:
            printList(head)

# } Driver Code Ends 