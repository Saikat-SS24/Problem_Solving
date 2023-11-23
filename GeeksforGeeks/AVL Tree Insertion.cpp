/* Given an AVL tree and N values to be inserted in the tree. Write a function to insert elements into the given AVL 
tree.

Note:
The tree will be checked after each insertion. 
If it violates the properties of balanced BST, an error message will be printed followed by the inorder traversal of 
the tree at that moment.
If instead all insertions are successful, inorder traversal of the tree will be printed.

Example 1:

Input:
N = 3
Values to be inserted = {5,1,4} 
Output:
1 4 5
Explanation:
Value to be inserted = 5
    5
Value to be inserted = 1
    5
   /
  1
Value to be inserted = 4
  5                     4
 /    LR rotation        /  \
1    ----------->       1   5
 \
 4
Therefore the inorder of the final tree will be 1, 4, 5.

Example 2:

Input:
N = 7
Values to be inserted = {21,26,30,9,4,14,28} 
Output:
4 9 14 21 26 28 30
Explanation:
Value to be inserted = 21
    21
Value to be inserted = 26
    21
     \
     26
Value to be inserted = 30
  21                        26
   \      LL rotation         /  \
   26    ----------->       21  30
    \
     30
Value to be inserted = 9
    26
   /  \
  21  30
 /
9
Value to be inserted = 4
      26                          26
     /  \                          /  \
    21  30                      9   30
   /          RR rotation        /  \
  9          ----------->       4  21
 /
4
Value to be inserted = 14
      26                          21
     /  \                          /  \
    9   30                      9   26
   / \          LR rotation      /  \    \
  4  21        ----------->    4  14  30
     /
    14
Value to be inserted = 28
      21                          21
     /  \                          /  \
    9   26                      9   28
   / \    \     RL rotation       / \    / \
  4  14   30   ----------->   4  14 26 30
          /
         28
Therefore the inorder of the final tree will be 4, 9, 14, 21, 26, 28, 30.
Your Task:  
You don't need to read input or print anything. Complete the function insertToAVL() which takes the root of the tree 
and the value of the node to be inserted as input parameters and returns the root of the modified tree.

Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(height of tree)

Constraints:
1 ≤ N ≤ 2000 */

//{ Driver Code Starts
//

#include <bits/stdc++.h>
#define MAXN 2000
using namespace std;

struct Node
{
    int data, height;
    Node *left, *right;
    
    Node(int x)
    {
        data=x;
        left=right=NULL;
        height=1;
    }
};

bool isBST(Node *n, int lower, int upper)
{
	if(!n) return 1;
	if( n->data <= lower || n->data >= upper ) return 0;
	return isBST(n->left, lower, n->data) && isBST(n->right, n->data, upper) ;
}

pair<int,bool> isBalanced(Node* n)
{
	if(!n) return pair<int,bool> (0,1);

	pair<int,bool> l = isBalanced(n->left);
	pair<int,bool> r = isBalanced(n->right);

	if( abs(l.first - r.first) > 1 ) return pair<int,bool> (0,0);

	return pair<int,bool> ( 1 + max(l.first , r.first) , l.second && r.second );
}

bool isBalancedBST(Node* root)
{
	if( !isBST(root, INT_MIN, INT_MAX) )
		cout<< "BST voilated, inorder traversal : ";

	else if ( ! isBalanced(root).second )
		cout<< "Unbalanced BST, inorder traversal : ";

	else return 1;
	return 0;
}

void printInorder(Node* n)
{
	if(!n) return;
	printInorder(n->left);
	cout<< n->data << " ";
	printInorder(n->right);
}


// } Driver Code Ends
/* The structure of the Node is
struct Node
{
    int data;
    Node *left;
    Node *right;
    int height;
};
*/

class Solution{
  public:
    /*You are required to complete this method */
    int height(Node *root) {
      if (!root)
        return 0;
    
      return root->height;
    }
    
    int getBalanceFactor(Node *root) {
      if (!root)
        return 0;
    
      return height(root->left) - height(root->right);
    }
    
    Node *leftRotate(Node *x) {
      Node *y = x->right;
      Node *z = y->left;
    
      y->left = x;
      x->right = z;
    
      x->height = max(height(x->left), height(x->right)) + 1;
      y->height = max(height(y->left), height(y->right)) + 1;
    
      return y;
    }
    
    Node *rightRotate(Node *x) {
      Node *y = x->left;
      Node *z = y->right;
    
      y->right = x;
      x->left = z;
    
      x->height = max(height(x->left), height(x->right)) + 1;
      y->height = max(height(y->left), height(y->right)) + 1;
    
      return y;
    }
    
    Node *LL(Node *root) { return root = rightRotate(root); }
    
    Node *LR(Node *root) {
      root->left = leftRotate(root->left);
      return root = rightRotate(root);
    }
    
    Node *RR(Node *root) { return root = leftRotate(root); }
    
    Node *RL(Node *root) {
      root->right = rightRotate(root->right);
      return root = leftRotate(root);
    }
    
    Node *createNode(int key) { return new Node(key); }
    
    Node *insertToAVL(Node *root, int data) {
      if (!root)
        return createNode(data);
    
      if (data < root->data)
        root->left = insertToAVL(root->left, data);
      else if (data > root->data)
        root->right = insertToAVL(root->right, data);
      else
        return root;
    
      int balance = getBalanceFactor(root);
      root->height = max(height(root->left), height(root->right)) + 1;
    
      if (balance > 1 and data < root->left->data)
        return LL(root);
    
      if (balance > 1 and data > root->left->data)
        return LR(root);
    
      if (balance < -1 and data > root->right->data)
        return RR(root);
    
      if (balance < -1 and data < root->right->data)
        return RL(root);
    
      return root;
    }

};

//{ Driver Code Starts.

int main()
{
	int ip[MAXN];
    
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        
        for(int i=0; i<n; i++)
            cin>> ip[i];
        
        Node* root = NULL;
        Solution obj;
        for(int i=0; i<n; i++)
        {
            root = obj.insertToAVL( root, ip[i] );
            
            if ( ! isBalancedBST(root) )
                break;
        }
        
        printInorder(root);
        cout<< endl;
    }
    return 0;
}
// } Driver Code Ends