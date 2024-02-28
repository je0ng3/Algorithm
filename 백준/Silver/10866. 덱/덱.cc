#include <iostream>
#include <algorithm>
#include <deque>
#include <cmath>
#include <string>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n; cin>>n;
  deque<int> dq;
  while(n--){
    string s; cin>>s;
    if(s.compare("push_front")==0){
      int x; cin>>x;
      dq.push_front(x);
    }
    else if(s.compare("push_back")==0){
      int x; cin>>x;
      dq.push_back(x);
    }
    else if(s.compare("pop_front")==0){
      if(dq.empty()){
        cout<<-1<<'\n';
      }else{
      cout<<dq.front()<<'\n';
      dq.pop_front();}
    }
    else if(s.compare("pop_back")==0){
      if(dq.empty()){
        cout<<-1<<'\n';
      }else{
      cout<<dq.back()<<'\n';
      dq.pop_back();}
    } 
    else if(s.compare("size")==0){
      cout<<dq.size()<<'\n';
    }
    else if(s.compare("empty")==0){
      if(dq.empty()) cout<<1<<'\n';
      else cout<<0<<'\n';
    }
    else if(s.compare("front")==0){
      if(dq.empty()){
        cout<<-1<<'\n';
      }else{
        cout<<dq.front()<<'\n';
      }
    }
    else if(s.compare("back")==0){
      if(dq.empty()){
        cout<<-1<<'\n';
      }else{
        cout<<dq.back()<<'\n';
      }
    }

  }
}