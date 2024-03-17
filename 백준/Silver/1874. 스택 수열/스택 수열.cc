#include <iostream>
#include <stack>
#include <queue>
using namespace std;

int x;
int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);
  
  int n, x, j=1; cin>>n;
  stack<int> s;
  queue<char> q;
  for(int i=1; i<=n; i++){
    cin>>x;
    while(s.empty()||s.top()!=x){
      if(j>n){
        cout<<"NO"<<'\n'; return 0;
      }
      s.push(j);
      q.push('+');
      j++;
    }
    q.push('-');
    s.pop();
  }
  while(!q.empty()){
    cout<<q.front()<<'\n';
    q.pop();
  }
  }