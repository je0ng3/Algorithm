#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n, k; cin>>n>>k;
  vector<int> v;
  for(int i=1; i<=n; i++){
    v.push_back(i);
  }
  cout<<'<';
  int idx=k-1;
  while(v.size()>1){
    cout<<v[idx];
    v.erase(v.begin()+idx);
    idx = (idx+k-1)%v.size();
    cout<<", ";
  }
  cout<<v.front()<<'>'<<'\n';
}