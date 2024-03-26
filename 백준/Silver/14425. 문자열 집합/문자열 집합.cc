#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n,m; cin>>n>>m;
  map<string, int> ma;
  while(n--){
    string s; cin>>s; ma[s]=1;
  }
  int count=0;
  while(m--){
    string s; cin>>s;
    if(ma.find(s)!=ma.end()){
      count++;
    }
  }
  cout<<count<<'\n';
  
}