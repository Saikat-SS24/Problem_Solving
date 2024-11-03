""" Given a linked list, you have to perform the following task:

Extract the alternative nodes starting from second node.
Reverse the extracted list.
Append the extracted list at the end of the original list.
Note: Try to solve the problem without using any extra memory.

Example 1:

Input:
LinkedList = 10->4->9->1->3->5->9->4
Output: 
10 9 3 9 4 5 1 4
Explanation: 
Alternative nodes in the given linked list are 4,1,5,4. Reversing the alternative nodes from the given list, and 
then appending them to the end of the list results in a list 10->9->3->9->4->5->1->4.
Example 2:

Input:
LinkedList = 1->2->3->4->5
Output: 
1 3 5 4 2 
Explanation:
Alternative nodes in the given linked list are 2 and 4. Reversing the alternative nodes from the given list, and 
then appending them to the end of the list results in a list 1->3->5->4->2.
Your Task:
You don't have to read input or print anything. Your task is to complete the function rearrange() which takes the 
head of the linked list as input and rearranges the list as required.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
0 <= Node_value <= 109 

  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None """


class Solution:
    def rearrange(self, head):
        # Code here
        if not head or not head.next or not head.next.next: return head
        first, second, altlast= head, head.next, head.next
        while second and second.next:
            first.next = second.next
            second.next = second.next.next
            first = first.next
            second = second.next
            
        prev = None
        curr = altlast
        
        while curr:
            nxt =curr.next
            curr.next = prev
            prev, curr = curr, nxt
            
        altlast = prev
        first.next = altlast
        return head

#{ 
 # Driver Code Starts
# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()



# Code execution starts here
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
            
        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
# } Driver Code Ends