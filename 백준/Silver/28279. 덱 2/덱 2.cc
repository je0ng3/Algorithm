#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n; cin>>n;
  deque<int> dq;
  while(n--){
    int x; cin>>x;
    if(x==1){
      cin>>x;
      dq.push_front(x);
    }
    else if(x==2){
      cin>>x;
      dq.push_back(x);
    }
    else if(x==3){
      if(dq.empty()){
        cout<<-1<<'\n';
      }else{
      cout<<dq.front()<<'\n';
      dq.pop_front();}
    }
    else if(x==4){
      if(dq.empty()){
        cout<<-1<<'\n';
      }else{
      cout<<dq.back()<<'\n';
      dq.pop_back();}
    } 
    else if(x==5){
      cout<<dq.size()<<'\n';
    }
    else if(x==6){
      if(dq.empty()) cout<<1<<'\n';
      else cout<<0<<'\n';
    }
    else if(x==7){
      if(dq.empty()){
        cout<<-1<<'\n';
      }else{
        cout<<dq.front()<<'\n';
      }
    }
    else if(x==8){
      if(dq.empty()){
        cout<<-1<<'\n';
      }else{
        cout<<dq.back()<<'\n';
      }
    }

  }
}