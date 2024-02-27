#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int a[1000000];
  for(int i=2; i<1000000; i++){
    a[i]=i;
  }
  for(int i=2; i<1000000; i++){
    if(a[i]==0){
      continue;
    }
    for(int j=i*2; j<1000000; j+=i){
      a[j]=0;
    }
  }

  int n; cin>>n;
  int count=0;
  for(int i=2; i<1000000; i++){
    if(a[i]!=0) count++;
    if(n==count) {
      cout<<a[i]<<'\n';
      break;
    }
  
  }
}