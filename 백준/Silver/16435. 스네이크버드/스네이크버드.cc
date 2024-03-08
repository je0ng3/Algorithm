#include <iostream>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;



int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  
  int n, l; cin>>n>>l;
  priority_queue<int, vector<int>, greater<int>> pq;
  while(n--){
    int h; cin>>h;
    pq.push(h);
  }
  while(!pq.empty()){
    if(pq.top()<=l) l++;
    else break;
    pq.pop();
  }
  cout<<l<<'\n';
}

