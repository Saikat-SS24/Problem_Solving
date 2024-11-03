""" Given a singly linked list of length n. The link list represents a binary number, ie- it contains only 0s and 1s. 
Find its decimal equivalent.
The significance of the bits decreases with the increasing index in the linked list.
An empty linked list is considered to represent the decimal value 0. 

Since the answer can be very large, answer modulo 109+7 should be printed.

Example 1:
Input:
n = 3
Linked List = {0, 1, 1}
Output:
3
Explanation:
0*22 + 1*21 + 1*20 =  1 + 2 + 0 = 3

Example 2:
Input:
n = 4
Linked List = {1, 1, 1, 0}
Output:
14
Explanation:
1*23 + 1*22 + 1*21 + 0*20 =  8 + 4 + 2 + 0 = 14
Your Task:
You do not have to take any input or print anything. Complete the function decimalValue() which takes a head node of a 
linked list as an input parameter and returns decimal representation of it.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
0 <= n <= 100
Data of each node is either 0 or 1 """ 

# your task is to complete this function
# Function should return an integer value

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
def reverse(head):
    if(head == None or head.next == None):
        return head
    curr = head
    prev = None
    nxt = head.next
    while(nxt):
        curr.next = prev
        prev = curr
        curr = nxt
        nxt = nxt.next
    curr.next = prev
    return curr
    
class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        # Code here
        rhead = reverse(head)
 
        ans = 0
        pos = 0
        while rhead:
            ans = (ans % MOD+(rhead.data*(2**pos)) % MOD) % MOD
            rhead = rhead.next
            pos += 1
        return ans


#{ 
 # Driver Code Starts
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob=Solution()
        print(ob.decimalValue(list1.head))

# Contributed By: Harshit Sidhwa
# } Driver Code Ends