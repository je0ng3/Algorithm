#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <string>
#include <utility>
using namespace std;


int arr[1000001];
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n; cin>>n;
    stack<int> s;
    for(int i=0; i<n; i++){
        int m; cin>>m;
        arr[i]=m;
        while(true){
            if(s.empty()){
                s.push(i);
                break;
            }
            int inx = s.top();
            if(m>arr[inx]){
                arr[inx] = m;
                s.pop();
            }else{
                s.push(i);
                break;
            }
        }
    }
    while(!s.empty()){
        int i=s.top();
        arr[i] = -1;
        s.pop();
    }
    for(int j=0; j<n; j++){
        cout<<arr[j]<<' ';
    }
    
}