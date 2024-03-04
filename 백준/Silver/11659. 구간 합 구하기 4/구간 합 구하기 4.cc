#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n, m; cin>>n>>m;
  vector<int> v;
  int x; cin>>x; v.push_back(x);
  for(int i=1; i<n; i++){
    cin>>x;
    v.push_back(x+v[i-1]);
  }
  int i,j;
  while(m--){
    cin>>i>>j;
    int a = i>1? v[i-2]:0;
    cout<<v[j-1]-a<<'\n';
  }

  
  
}