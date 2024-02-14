#include <iostream>
#include <math.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int n; cin >> n;
  long long x;
  while(n--){
    cin>>x;
    long long r = sqrt(x);
    if(r*r!=x){
      cout<<0<<' ';
    }else{
      cout<<1<<' ';
    } 
  }
}