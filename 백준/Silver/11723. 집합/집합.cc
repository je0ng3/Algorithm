#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  
  int m; cin>>m;
  string s; int a;
  int ans[21]={0,};
  while(m--){
    cin>>s;
    if(s.compare("add")==0){
      cin>>a;
      ans[a]=1;
    }else if(s.compare("remove")==0){
      cin>>a; ans[a]=0;
    }else if(s.compare("check")==0){
      cin>>a; cout<<ans[a]<<'\n';
    }else if(s.compare("toggle")==0){
      cin>>a;
      if(ans[a]) ans[a]=0;
      else ans[a]=1;
    }else if(s.compare("all")==0){
      for(int i=1;i<=20;i++) ans[i]=1;
    }else fill_n(ans,21,0);
  }
  
}

