#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;


int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  
  map<string, string> ad;
  int n, m; 
  cin >> n >> m;
  string mail, password;
  while(n--){
    cin>>mail>>password;
    ad[mail]=password;
  }
  while(m--){
    cin>>mail;
    cout<<ad[mail]<<'\n';
  }
  
}

