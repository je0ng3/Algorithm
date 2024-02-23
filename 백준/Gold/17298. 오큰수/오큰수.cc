#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n; cin>>n;
    int seq[1000000];
    int nge[1000000]; fill_n(nge,1000000,-1);
    stack<int> s;
    for(int i=0; i<n; i++){
        cin>>seq[i];
    }
    for(int i=n-1; i>=0; i--){
        while(!s.empty() && s.top()<=seq[i])
            s.pop();
        if(!s.empty()) 
            nge[i]=s.top();
        s.push(seq[i]);
    }
    for(int i=0; i<n; i++){
        cout << nge[i] <<' ';
    }

}