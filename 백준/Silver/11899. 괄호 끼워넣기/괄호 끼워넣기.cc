#include <iostream>
#include <stack>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;


int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);
  
  string s; cin>>s;
  int l=0; int count=0;
  for(int i=0; i<s.length(); i++){
    if(s[i]=='(') l++;
    else {
      if(l>0) l--;
      else count++;
    }
  }
  cout<<l+count<<'\n';
  
}