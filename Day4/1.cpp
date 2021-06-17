#include<iostream>
// #include<bits/stdc++.h>
using namespace std ;

int main(){

    string col;
    cin>>col;

    int n = col.length();
    int sum = 0;

    int m_times = 1;
    int multiple = 1;

    for(int i=1; i <= n ; i++ ){
        if(m_times <= n && m_times > 1){
            multiple = multiple*26;
            m_times = m_times + 1;
            cout<<"Hii"<<endl;
        }
        if(m_times == 1){
            m_times = m_times + 1;
            cout<<"Hii"<<endl;
        }

        sum += multiple*(int(col[n-i])%64);

        cout<<multiple<<" "<<m_times<<" "<<sum<<endl;        
    }
    cout<<sum<<endl;
    return 0;
}

// Z A 
//     26(Tens)*26(Z) + 0(Units)*1(A)
// A Z
// 26(Tens) * 1(A) + 26(Z)

// A A
// 26(Tens) * 1(A) + 1(A)