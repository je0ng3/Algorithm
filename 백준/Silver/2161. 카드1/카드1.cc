#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  deque<int> dq;
  int n; cin>>n;
  for(int i=1; i<=n; i++){
    dq.push_back(i);
  }
  while(!dq.empty()){
    cout<<*dq.begin()<<' ';
    dq.pop_front();
    if(dq.empty()) break;
    dq.push_back(*dq.begin());
    dq.pop_front();
  }

}