#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
using namespace std;

int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int n; cin>>n;

  vector<int> a;
  a.resize(n+1);
  for(int i=2; i<=n; i++){
    a[i]=i;
  }
  for(int i=2; i<=n; i++){
    if(a[i]==0){
      continue;
    }
    for(int j=i*2; j<=n; j+=i){
      a[j]=0;
    }
  }
  a.erase(remove(a.begin(), a.end(), 0), a.end());
  int count=0;
  vector<int> v;
  for(int i=a.size()-1; i>0; i--){
    if(a[i]>n) continue;
    v.push_back(a[i]);
    while(true){
      if(accumulate(v.begin(), v.end(),0)==n){
        count++;
        break;
      }
      else if(accumulate(v.begin(), v.end(),0)>n)
        break;
      v.push_back(a[i-1]);
      i--;
    }
    v.erase(v.begin());

  }
  if(n==2) count++;
  cout<<count<<'\n';
}

