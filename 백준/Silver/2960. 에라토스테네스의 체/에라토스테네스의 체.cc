#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n, k; cin>>n>>k;
  int a[1001];
  for(int i=2; i<=n; i++){
    a[i]=i;
  }
  int p=2;
  for(int i=2; i<=n; i++){
    if(a[i]==0){
      continue;
    }
    for(int j=i; j<=n; j+=i){
      if(a[j]!=0){
        k--;
        if(k==0){
          cout<<j<<'\n';
          return 0;
        }
        a[j]=0;
      }
    }
    
  }

}