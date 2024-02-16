#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int n; cin>> n;
  int jh=n, sm=n;
  vector<int> v;
  int x;
  for(int i=0; i<14; i++){
    cin >> x;
    v.push_back(x);
  }
  int bnp=0, md=0;
  for(int i=0; i<14; i++){
    if(jh==0){
      break;
    }
    bnp+=(jh/v[i]);
    jh=(jh%v[i]);
  }
  for(int i=0; i<14; i++){
    if(i>3 && sm>0 && ((v[i-3]>v[i-2])&&(v[i-2]>v[i-1])&&(v[i-1]>v[i])) ){
      md+=(sm/v[i]);
      sm=(sm%v[i]);
    } else  if(i>3 && md>0 && ((v[i-3]<v[i-2])&&(v[i-2]<v[i-1])&&(v[i-1]<v[i])) ){
      sm=(md*v[i]);
      md=0;
    } 
  }
  int tot_jh = jh+(v[13]*bnp);
  int tot_sm = sm+(v[13]*md);
  if(tot_jh>tot_sm){
    cout << "BNP";
  } else if(tot_jh<tot_sm){
    cout << "TIMING";
  } else{
    cout << "SAMESAME";
  }
    
  
}