#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

struct cmp{
    bool operator()(pair<int, int>&a, pair<int, int>&b){
        if(a.second==b.second)
            return a.first<b.first;
        else
            return a.second<b.second;
    }
};

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    priority_queue<pair<int, int>,vector<pair<int,int>>,cmp> p;
    priority_queue<int, vector<int>, greater<int>> ans;
    for(int i=1; i<=8; i++){
        int a; cin>>a;
        p.push({i, a});
    }
    int sum=0;
    for(int i=0; i<5; i++){
        sum+=p.top().second;
        ans.push(p.top().first);
        p.pop();
    }
    cout<<sum<<'\n';
    for(int i=0; i<5; i++){
        cout<<ans.top()<<' ';
        ans.pop();
    }
}