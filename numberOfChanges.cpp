#include<iostream>
#include<bits/stdc++.h>
#define long long ll;
using namespace std; 

int numberOfChanges(int* arr,int n){
    
    int numberOfChange = 0;
    int hashMap[100];

    memset(hashMap,0,sizeof(hashMap));

    int max = 0;
    //check of for max element 
    for(int i=0;i<n;i++){
        hashMap[arr[i]] += 1;
        if(hashMap[arr[i]] >= hashMap[arr[max]]){
            max = i;
        }
    }
    cout<<arr[max]<<endl;

    return(arr[max]);
}

int main(){

    // string input;
    // getline(cin,input);

    // int n = input.length();

    // bool dp[n][n];
    // memset(dp, 0, sizeof(dp));
    // arr = [1, 5, 2, 1, 3, 2, 1]

    int n;
    cin>>n;

    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    numberOfChanges(arr,n);

   return 0; 
}