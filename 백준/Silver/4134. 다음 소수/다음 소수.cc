#include <iostream>
using namespace std;

long long pn_(long long m){
  if (m<=2) return 2;
  for (long long i=(m+(m%2==0));; i+=2){
    int pn = 0;
    for (long long j=3; j*j<=i; j++){
      if (i%j==0){
        pn = 1;
        break;
      }
    }
    if (pn == 0 && i>1){
      return i;
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int n; cin >> n;
  long long a;
  while(n--){
    cin >> a;
    cout<<pn_(a)<<endl;
  }
}