#include<bits/stdc++.h>
using namespace std;

int main(){
    int T;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin>>arr[i];
        }
        int target; 
        cin>>target;
        int hashArr[10000];
        for(int i=0;i<n;i++){
            hashArr[arr[i]] = i;
        }
        for(int i=0;i<n;i++){
            int rem = target - arr[i];
            if(hashArr[rem]){
                cout<<i<<" "<<hashArr[rem]<<endl;
            }
        }
    }
}