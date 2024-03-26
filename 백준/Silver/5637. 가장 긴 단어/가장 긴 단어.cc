#include <iostream>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  string s, s_word; cin>>s;
  int s_long = 0; 
  while(s.compare("E-N-D")!=0){
    int first=0, count=0;
    for(int i=0; i<s.length(); i++){
      if(s[i]==45 || (s[i]>=65 && s[i]<=90) || (s[i]>=97 && s[i]<=122)){
        count++;
      }else{
        if(count>s_long){
          s_long = count;
          s_word = s.substr(first, i);
        }
        count = 0;
        first = i+1;
      }
    }
    if(count!=0){
      if(count>s_long){
          s_long = count;
          s_word = s.substr(first, s.length());
        }
    }
    cin>>s;
  }
  for(int i=0; i<s_long; i++){
    s_word[i] = tolower(s_word[i]);
  }
  cout<<s_word<<'\n';
}