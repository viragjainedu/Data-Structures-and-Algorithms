
#include<iostream>
using namespace std;

struct Node{
    int data;
    char c;
    struct Node* left = NULL;
    struct Node* right = NULL;
};

Node* createRoot(int data,char c){
    Node* temp = new Node();
    temp->data = data;
    temp->c = c;
    return temp;
}

int main (){

    // Node* L;
    // Node* R;
    // L = new Node();
    // R = new Node();
    // Node N = {5,'a',L,R};
    
    // cout<<(N.data)<<endl;
    // cout<<(N.c)<<endl;
    
    // cout<<(N.left->data)<<endl;
    // cout<<(N.left->c)<<endl;
    
    // cout<<(N.right->data)<<endl;
    // cout<<(N.right->c)<<endl;

    Node* Root = createRoot(4,'a') ; 
    Root->left = createRoot(5,'b');
    Root->right = createRoot(6,'c');
    cout<<(Root->data);
    cout<<(Root->left->data);
    cout<<(Root->right->data);
    return 0;
}

Node L  .
Node* L  ->