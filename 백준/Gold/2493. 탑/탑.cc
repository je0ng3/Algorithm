#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n; cin>>n;
    int ans[500000] = {0};
    int seq[500000];
    stack<int> s, s2;
    for(int i=0; i<n; i++){
        cin>>seq[i];
    }
    for(int i=0; i<n; i++){
        while(!s.empty()&&s.top()<seq[i]){
            s.pop();
            s2.pop();
        }
        if(!s.empty())
            ans[i] = s2.top();
        s.push(seq[i]);
        s2.push(i+1);
    }
    for(int i=0; i<n; i++){
        cout << ans[i] << ' ';
    }


}