// preorder iterative traversal tree bst
#include<iostream>
#include<bits/stdc++.h>
using namespace std;

struct Node{
    int data;
    struct Node* left = NULL;
    struct Node* right = NULL;
};

Node* creatNode(int data){
    Node* temp = new Node();
    temp->data = data;
    return temp;
}

Node* insertBST(Node* Root,int data){
    if(Root == NULL){
        Root = creatNode(data);
        return Root;
    }

    Node* temp = Root;
    while(1){
        if(data <= temp->data){
            if(temp->left == NULL){
                temp->left = creatNode(data);
                return temp->left;
            }
            else{
                temp = temp->left;
            }
        }
        else if(data >= temp->data){
            if(temp->right == NULL){
                temp->right = creatNode(data);
                return temp->right;
            }
            else{
                temp = temp->right;
            }
        }   
    }
}

void PrintTopToBottom(Node* leaf , map<Node*, Node*> parent){

    stack<int> path;

    while(leaf){
        path.push(leaf->data);
        leaf = parent[leaf];
    }

    while(!path.empty()){
        cout<<path.top()<<" ";
        path.pop();
    }
    cout<<endl;


}


void IterPreOrder(Node* temp){
    
    stack<Node*> s;
    s.push(temp);
    map<Node* , Node*> parent;
    parent[temp] = NULL;

    while(!s.empty() || temp != NULL){

        temp = s.top();
        // cout<<temp->data<<" ";
        s.pop();
// 9 
// 10 5 15 3 8 12 18 7 9 

        if(temp->right != NULL){
            parent[temp->right] = temp;
            s.push(temp->right);
        }
        if(temp->left != NULL){
            parent[temp->left] = temp;
            s.push(temp->left);
        }
        if(temp->left == NULL && temp->right == NULL){
            PrintTopToBottom(temp,parent);
        }

    }
    
}

int main (){

    //initialize
    Node* Root = NULL; 

    int N;
    cin>>N;
    int numbers[N];

    Node* temp;
    cin>>numbers[0];
    Root = insertBST(Root,numbers[0]);
    temp = Root;

    for(int i=1;i<N;i++){
        cin>>numbers[i];
        temp = insertBST(Root,numbers[i]);
    }


    IterPreOrder(Root);

    return 0;
}

