#include<iostream>
#include<bits/stdc++.h>

using namespace std; 

int main(){

    string input;
	getline(cin,input);

    stack<string> s;
    string str = "";
    for(int i=0;    i<input.length();   i++){
        if(input[i] == ' '){
            s.push(str);
            // cout<<str<<endl;
            str = "";
        }
        else{
            str += input[i];
        }
    }
    s.push(str);

    while(!s.empty()){
        cout<<s.top()<<" ";
        s.pop();
    }

    return 0; 
}