#include<iostream>
#include<bits/stdc++.h>

using namespace std;

void Merge(int* arr,int n, int start, int mid ,int end){
    
}

void MergeSort(int* arr,int n, int start, int end ){
    if(start == end){
        return arr[start];
    }

    int mid = start + (end-start)/2
    MergeSort(arr, n, start, mid);
    MergeSort(arr, n, mid+1, end);
    Merge(arr,n,start,mid,end);
    
}   

int main(){

    int n;
    cin>>n;
    int arr[n];
    for(int i=0; i<n ; i++){
        cin>>arr[i];
    }

    MergeSort(arr,n,0,n-1);

    return 0;
}