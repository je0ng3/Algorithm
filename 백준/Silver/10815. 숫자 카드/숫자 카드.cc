#include <iostream>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  
  int n; cin>>n;
  map <int, int> ma;
  for(int i=0; i<n; i++){
    int x; cin>>x;
    ma[x]=1;
  }
  int m; cin>>m;
  while(m--){
    int x; cin>>x;
    if(ma.find(x)==ma.end()) cout<<0<<' ';
    else cout<<1<<' ';
  }
}