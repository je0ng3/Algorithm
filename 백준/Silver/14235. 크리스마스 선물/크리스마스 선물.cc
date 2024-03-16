#include <iostream>
#include <queue>
using namespace std;

int x;
int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);
  
  int t, n, a; cin>>t;
  priority_queue<int> pq;
  while(t--){
    cin>>n; 
    if(n==0){
      if(pq.empty()) cout<<-1<<'\n';
      else{
        cout<<pq.top()<<'\n';
        pq.pop();
      }
    }else{
      while(n--){
        cin>>a; pq.push(a);
      }
    }
  }

  }