/* Given a binary tree and the task is to find the spiral order traversal of the tree.
Spiral order Traversal mean: Starting from level 0 for root node, for all the even levels we print the node's value 
from right to left and for all the odd levels we print the node's value from left to right. 

Example 1:

Input:
      1
    /   \
   3     2
Output:1 3 2

Example 2:

Input:
           10
         /     \
        20     30
      /    \
    40     60
Output: 10 20 30 60 40 
*/

//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// Tree Node
struct Node
{
    int data;
    Node* left;
    Node* right;
};
// Utility function to create a new Tree Node
Node* newNode(int val)
{
    Node* temp = new Node;
    temp->data = val;
    temp->left = NULL;
    temp->right = NULL;

    return temp;
}

vector<int> findSpiral(Node *root);

// Function to Build Tree
Node* buildTree(string str)
{
    // Corner Case
    if(str.length() == 0 || str[0] == 'N')
        return NULL;

    // Creating vector of strings from input
    // string after spliting by space
    vector<string> ip;

    istringstream iss(str);
    for(string str; iss >> str; )
        ip.push_back(str);

    // Create the root of the tree
    Node* root = newNode(stoi(ip[0]));

    // Push the root to the queue
    queue<Node*> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while(!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node* currNode = queue.front();
        queue.pop();

        // Get the current node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if(currVal != "N") {

            // Create the left child for the current node
            currNode->left = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if(i >= ip.size())
            break;
        currVal = ip[i];

        // If the right child is not null
        if(currVal != "N") {

            // Create the right child for the current node
            currNode->right = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}


int main() {
    int t;
    string  tc;
    getline(cin,tc);
    t=stoi(tc);
    while(t--)
    {
        string s;
        getline(cin,s);
        Node* root = buildTree(s);

        vector<int> vec = findSpiral(root);
        for(int x : vec)
        cout<<x<<" ";
        cout << endl;
    }
    return 0;
}



// } Driver Code Ends


/* A binary tree node has data, pointer to left child
   and a pointer to right child  
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
}; */


//Function to return a list containing the level order traversal in spiral form.
vector<int> findSpiral(Node *root)
{
    //Your code here
    deque<pair<int,Node*>> q;
    q.push_back({0, root});
    
    vector<int> ans;
    
    int curlevel = 0;
    
    while(!q.empty()){
        int level;
        Node * node;
        
        if(curlevel & 1){
            if(q.front().first != curlevel)
                ++curlevel;
        }
        else{
            if(q.back().first != curlevel)
                ++curlevel;
        }
        
        if(curlevel & 1){
            tie(level, node) = q.front();
            q.pop_front();
        }
        else{
            tie(level, node) = q.back();
            q.pop_back();
        }
        
        ans.push_back(node -> data);
        
        if(level & 1){
            if(node -> left != nullptr)
                q.push_back({level + 1, node -> left});
            if(node -> right != nullptr)
                q.push_back({level + 1, node -> right});
        }
        else{
            if(node -> right != nullptr)
                q.push_front({level + 1, node -> right});
            if(node -> left != nullptr)
                q.push_front({level + 1, node -> left});
        }
    }
    
    return ans;
    	 
}
