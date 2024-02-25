#include <iostream>
#include <stack>
using namespace std;

    

int main(){
  int n; cin>>n;
  stack<int> s;
  while(n--){
    int a,b; cin>>a>>b;
    s.push(b);
  }
  int count=0, min=s.top()+1;
  while(!s.empty()){
    if(s.top()<=min){
        min=s.top();
        count++;
    }
    s.pop();
  }
  cout<<count<<'\n';
}
