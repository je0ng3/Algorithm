#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  string s; cin>>s;
  int len = s.length();
  string a = "AAAA", b = "BB";
  string result = "";
  while(len>0){
    if(s[result.length()]=='.'){
      len--;
      result+='.';
    }
    else if(len>=4 && s[result.length()+1]!='.'
      && s[result.length()+2]!='.' && s[result.length()+3]!='.'){
      result+=a;
      len-=4;
    }else if(len>=2 && s[result.length()+1]!='.'){
    result+=b;
    len-=2;
    }else{
      cout<<-1<<'\n';
      return 0;
    }
  }
  cout<<result<<'\n';


}