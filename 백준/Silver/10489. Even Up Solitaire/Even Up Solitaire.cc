#include <iostream>
#include <stack>
using namespace std;

    

int main(){
  int n; cin>>n;
  stack<int> s;
  while(n--){
    int a; cin>>a;
    if(!s.empty()){
        if((s.top()+a)%2==0)
            s.pop();
        else
            s.push(a);
    }else{
        s.push(a);
    }
  }
  cout<<s.size()<<'\n';
}
