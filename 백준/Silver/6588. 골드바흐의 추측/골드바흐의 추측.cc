#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int a[1000001];
  for(int i=2; i<=1000000; i++){
    a[i]=i;
  }
  for(int i=2; i<=1000000; i++){
    if(a[i]==0){
      continue;
    }
    for(int j=i*2; j<=1000000; j+=i){
      a[j]=0;
    }
  }
  while(true){
    int n; cin>>n;
    if(n==0) break;
    int check=0;
    for(int i=n-2;i>=2;i--){
      if(a[i]==0) continue;
      if(a[n-a[i]]!=0){
        cout<<n<<" = "<<n-i<<" + "<<i<<'\n';
        check=1;
        break;
      }
    }
    if(!check)
      cout << "Goldbach's conjecture is wrong."<<'\n';
  }

}