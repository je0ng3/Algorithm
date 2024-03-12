#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

class cmp{
  public:
    bool operator()(const pair<int, int> &a, const pair<int, int>&b) const{
      if(a.second==b.second)
        return a.first>b.first;
      return a.second>b.second;
    }
};

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  
  int n; cin>>n;
  priority_queue<pair<int,int>, vector<pair<int, int>>, cmp> pq;
  for(int i=0; i<n; i++){
    int a, b; cin>>a>>b;
    pq.push(make_pair(a,b));
  }
  for(int i=0; i<n; i++){
    cout<<pq.top().first<<' '<<pq.top().second<<'\n';
    pq.pop();
  }
}

