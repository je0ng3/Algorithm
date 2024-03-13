#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n, m; cin>>n>>m;
  queue<int> q;
  int sum=0, count=0, x;
  while(n--){
    cin>>x; 
    sum+=x; q.push(x);
    while(sum>m) {
      sum-=q.front(); q.pop();
    }
    if(sum==m){
      count++;
      sum-=q.front(); q.pop();
    }
  }
  cout<<count<<'\n';
  
}