#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  string s; cin>>s;
  priority_queue<int> pq;
  for(int i=0; i<s.size(); i++){
    pq.push((int)(s[i]-'0'));
  }
  
  while(!pq.empty()){
    cout<<pq.top();
    pq.pop();
  }
  
}