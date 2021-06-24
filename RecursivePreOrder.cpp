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

void RecursivePreOrder(Node* temp){

    if(temp == NULL){
        return ;
    }

    cout<<temp->data<<" ";
    RecursivePreOrder(temp->left);
    RecursivePreOrder(temp->right);
// 10 5 15 3 8 12 18 7 9 
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


    RecursivePreOrder(Root);

    return 0;
}

