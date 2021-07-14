// Using DP approach.. O(n2)
#include<iostream>
#include<bits/stdc++.h>

using namespace std; 

void printSubStr(string str, int low, int high)
{
    for (int i = low; i <= high; ++i)
        cout << str[i];
}

int main(){

    string input;
    getline(cin,input);

    int n = input.length();

    bool dp[n][n];
    memset(dp, 0, sizeof(dp));
    

    // for(int i=0;i<n;i++){
    //     for(int j=0;j<n;j++){
    //         cout<<dp[i][j]<<" ";
    //     }
    //     cout<<endl;
    // }

    //for substring length 1
    for(int i=0;i<=n;i++){
        dp[i][i] = true;
    }

    //for substring length 2
    int start = 0;
    int maxLength = 0;

    for (int i = 0; i < n - 1; ++i) {
        if (input[i] == input[i + 1]) {
            dp[i][i + 1] = true;
            start = i;
            maxLength = 2;
        }
    }

    // Check for lengths greater than 2.    
    // k is length of substring
    for (int k = 3; k <= n; ++k) {
        // Fix the starting index
        for (int i = 0; i < n - k + 1; ++i) {
            // Get the ending index of substring from
            // starting index i and length k
            int j = i + k - 1;
 
            // checking for sub-string from ith index to
            // jth index iff input[i+1] to input[j-1] is a
            // palindrome
            if (dp[i + 1][j - 1] && input[i] == input[j]) {
                dp[i][j] = true;
 
                if (k > maxLength) {
                    start = i;
                    maxLength = k;
                }
            }
        }
    }
    
    cout << "Longest palindrome substring is: ";
    printSubStr(input, start, start + maxLength - 1);
 
   return 0; 
}